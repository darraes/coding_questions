import asyncio
import re
import urllib.error
import urllib.parse
from aiohttp import ClientSession

HREF_RE = re.compile(r'href="(.*?)"')


class HttpCrawler:
    def __init__(self, queue: asyncio.Queue, workers: int = 5):
        self.queue = queue
        self.w_count = workers
        self.workers = []
        self.visited = set()
        self.crawled = []

    async def craw(self):
        async with ClientSession() as session:
            for i in range(self.w_count):
                self.workers.append(asyncio.create_task(self.worker(str(i), session)))

            await asyncio.gather(*self.workers, return_exceptions=True)

    async def worker(self, wid, session: ClientSession):
        while True:
            url, depth = await self.queue.get()
            self.crawled.append((wid, depth, url))

            if depth < 3:
                for next_url in await self.crawl_url(url, session):
                    self.visited.add(next_url)
                    await self.queue.put((next_url, depth + 1))

            self.queue.task_done()
            await asyncio.sleep(0.001)
            if self.queue.empty():
                break

    async def crawl_url(self, url: str, session: ClientSession, **kwargs):
        exclude = ["png", "ico", "xml", "css"]
        next_urls = set()

        html = await self.fetch_html(url, session, **kwargs)
        for link in HREF_RE.findall(html):
            if any(x in link for x in exclude) or link in self.visited:
                continue
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError):
                print("Error parsing URL: %s", link)
            else:
                next_urls.add(abslink)
                if len(next_urls) == 3:
                    break
        return next_urls

    async def fetch_html(self, url: str, session: ClientSession, **kwargs) -> str:
        resp = await session.request(method="GET", url=url, **kwargs)
        resp.raise_for_status()
        html = await resp.text()
        return html


if __name__ == "__main__":
    queue = asyncio.Queue()
    crawler = HttpCrawler(queue, workers=10)
    queue.put_nowait(("https://www.nytimes.com/guides/", 0))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(crawler.craw())

    for c in crawler.crawled:
        print(c)

