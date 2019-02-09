from collections import deque
import asyncio

###########################################################
###########################################################
# IMPORTANT: This code doesn't run. This is just a concept
###########################################################
###########################################################


class WGet:
    FOREVER = -1

    def __init__(self):
        self.queue = Queue()
        self.w_count = 10
        self.visited = set()
        self.workers = []
        self.last_status = [False] * self.w_count

    async def fetch(self, url):
        """
        rtype: list<urls>
        """
        pass

    def none_found(self):
        # return is they are all false
        pass

    def stop(self):
        for w in self.workers:
            w.stop()

    async def craw(self, url, max_depth=-1):
        await self.queue.put(0, url)
        self.found = True

        for i in range(self.w_count):
            self.workers.append(asyncio.create_task(self.craw_url(i)))

        await asyncio.gather(self.workers)
        return self.visited

    async def craw_url(self, id, max_depth=-1):
        try:
            while not self.none_found():
                self.last_status[id] = False
                n_url, depth = await self.queue.get()

                self.last_status[id] = True
                urls = await self.fetch(n_url)

                if not len(urls):
                    self.last_status[id] = False

                n_depth = depth + 1

                if n_depth >= max_depth and max_depth != WGet.FOREVER:
                    break

                for u in urls:
                    if u not in self.visited:
                        self.visited.add(u)
                        await self.queue.put((u, depth + 1))

        except Exception:
            print("Task stop requested")

        self.stop()

