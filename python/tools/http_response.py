import aiohttp
import asyncio
import timeit
import time
import requests

# BASE_URL = "http://localhost:5002/fetch"
BASE_URL = "http://localhost:8000/fetch"
URL = "https://jsonplaceholder.typicode.com/comments"


def build_urls():
    return [f"{BASE_URL}?url={URL}/{x}" for x in range(8)]


class Statistics:
    def __init__(self):
        self.runners = []
        self.max_runner = None
        self.min_runner = None
        self.total_runners = 0
        self.start_time = time.time()

    def add_runner(self, runner):
        self.runners.append(runner)

    def end_time(self):
        self.elapsed_time = (time.time() - self.start_time)

    def compare_runners(self):
        self.min_runner = self.runners[0].time
        self.max_runner = self.runners[0].time
        for runner in self.runners:
            self.total_runners += runner.time
            if runner.time < self.min_runner:
                self.min_runner = runner.time
            elif runner.time > self.max_runner:
                self.max_runner = runner.time

    def display_stats(self):
        self.compare_runners()

        for runner in self.runners:
            print(runner)

        print(f"MIN TIME: {self.min_runner}")
        print(f"MAX TIME: {self.max_runner}")
        print(f"SUM: {self.total_runners}")

    def sort_runners(self):
        self.runners = sorted(self.runners, key=lambda k: k.time) 


class Runner:
    def __init__(self, response, start_time):
        self.url = response.url
        self.status = response.status
        self.start_time = start_time
        self.end_time = time.time()
        self.time = self.end_time - self.start_time

    def __str__(self):
        return f"url: {self.url} \tstatus: {self.status} \ttime: {self.time}"


async def fetch_url(url, session):
        start = time.time()
        async with session.get(url) as response:
            runner = Runner(response, start)

        return runner


async def get_stats(urls):
    stats = Statistics()

    async with aiohttp.ClientSession() as session:
        stats.runners = await asyncio.gather(*[fetch_url(u, session) for u in urls])

    stats.end_time()

    return stats


def main():
    urls = build_urls()
    stats = asyncio.run(get_stats(urls))
    stats.sort_runners()
    stats.display_stats()


if __name__ == '__main__':
    main()
    
    