import asyncio
import re
import urllib.error
import urllib.parse
from aiohttp import ClientSession

HREF_RE = re.compile(r'href="(.*?)"')


class HttpCrawler:
    def __init__(
        self,
        queue: asyncio.Queue,
        start_urls,
        workers: int = 5,
        exclude_extensions=["png", "ico", "xml", "css", "jpeg", "jpg"],
        max_depth=3,
        max_links_per_page=3,
    ):
        self.queue = queue
        self.w_count = workers
        self.exclude_extensions = exclude_extensions
        self.max_depth = max_depth
        self.max_links_per_page = max_links_per_page
        self.workers = []
        self.visited = set()
        self.crawled = []

        for url in start_urls:
            self.queue.put_nowait((url, 0))
            self.visited.add(url)

    async def craw(self):
        async with ClientSession() as session:
            for i in range(self.w_count):
                self.workers.append(asyncio.create_task(self.worker(str(i), session)))

            await asyncio.gather(*self.workers, return_exceptions=True)

    async def worker(self, wid, session: ClientSession):
        while True:
            url, depth = await self.queue.get()
            self.crawled.append((wid, depth, url))

            if depth < self.max_depth:
                for next_url in await self.crawl_url(url, session):
                    await self.queue.put((next_url, depth + 1))

            self.queue.task_done()
            await asyncio.sleep(0.001)
            if self.queue.empty():
                break

    async def crawl_url(self, url: str, session: ClientSession, **kwargs):
        next_urls = set()

        html = await self.fetch_html(url, session, **kwargs)
        for link in HREF_RE.findall(html):
            if any(x in link for x in self.exclude_extensions):
                continue

            try:
                abslink = urllib.parse.urljoin(url, link)
                abslink, _ = urllib.parse.urldefrag(abslink.strip("/"))
            except (urllib.error.URLError, ValueError):
                print("Error parsing URL: %s", link)
            else:
                if abslink in self.visited:
                    continue

                self.visited.add(abslink)
                next_urls.add(abslink)
                if len(next_urls) == self.max_links_per_page:
                    break
        return next_urls

    async def fetch_html(self, url: str, session: ClientSession, **kwargs) -> str:
        resp = await session.request(method="GET", url=url, **kwargs)
        resp.raise_for_status()
        html = await resp.text()
        return html


if __name__ == "__main__":
    queue = asyncio.Queue()
    crawler = HttpCrawler(
        queue, start_urls={"https://www.nytimes.com/guides/"}, workers=10
    )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(crawler.craw())

    for c in crawler.crawled:
        print(c)

