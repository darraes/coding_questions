import asyncio
import re
import urllib.error
import urllib.parse
from threading import Thread, currentThread
from time import sleep

import async_timeout
from aiohttp import ClientSession

HREF_RE = re.compile(r'href="(.*?)"')


class HttpCrawler:
    def __init__(
        self,
        queue: asyncio.Queue,
        start_urls,
        workers: int = 5,
        exclude_keys=[
            "png",
            "ico",
            "xml",
            "css",
            "jpeg",
            "jpg",
            "mailto",
            "android",
            "tel",
            "javascript",
        ],
        max_depth=3,
        max_links_per_page=3,
    ):
        self.queue = queue
        self.workers_count = workers
        self.exclude_keys = exclude_keys
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
            for i in range(self.workers_count):
                self.workers.append(asyncio.create_task(self._run(str(i), session)))

            await asyncio.gather(*self.workers)

    def cancel(self):
        for worker in self.workers:
            worker.cancel()

    async def _run(self, wid, session: ClientSession):
        try:
            while True:
                url, depth = await self.queue.get()
                self.crawled.append((currentThread().ident, wid, depth, url))

                if depth < self.max_depth:
                    urls = await self._crawl_url(url, session)
                    for next_url in urls:
                        await self.queue.put((next_url, depth + 1))

                self.queue.task_done()
        except asyncio.CancelledError:
            print("Worker cancelled")

    async def _crawl_url(self, url: str, session: ClientSession, **kwargs):
        next_urls = set()
        try:
            html = await self._fetch_html(url, session, **kwargs)
            for link in HREF_RE.findall(html):
                if any(x in link for x in self.exclude_keys):
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
        except Exception as e:
            print("Error on", url, e)
        return next_urls

    async def _fetch_html(self, url: str, session: ClientSession, **kwargs) -> str:
        with async_timeout.timeout(10):
            resp = await session.request(method="GET", url=url, **kwargs)
            resp.raise_for_status()
            html = await resp.text()
            return html


if __name__ == "__main__":
    crawlers = []

    def start_crawler(start_urls):
        global crawlers
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        queue = asyncio.Queue()
        crawler = HttpCrawler(queue, start_urls=start_urls, workers=10, max_depth=4)
        crawlers.append(crawler)

        # asyncio.run(crawler.craw())
        loop.run_until_complete(crawler.craw())
        loop.stop()

        for c in crawler.crawled:
            print(c)

    tasks = [
        Thread(
            target=start_crawler,
            args=({"https://www.nytimes.com/guides/", "https://www.cnn.com/"},),
        ),
        Thread(
            target=start_crawler,
            args=({"https://www.bloomberg.com/markets/economics"},),
        ),
    ]

    for t in tasks:
        t.start()

    sleep(10)

    for c in crawlers:
        print("Canceling")
        c.cancel()

    for t in tasks:
        t.join()
