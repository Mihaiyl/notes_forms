import httpx
import time
import asyncio

URLS = ["http://127.0.0.1:8000/"]
def test_sync():
    start_total = time.perf_counter()
    with httpx.Client() as client:
        for url in URLS:
            start = time.perf_counter()
            client.get(url)
            print(f"Sync {url}: {time.perf_counter() - start:.4f}s")
    print(f"Total Sync Time: {time.perf_counter() - start_total:.4f}s")

async def test_async():
    total_start = time.perf_counter()
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in URLS]
        responses = await asyncio.gather(*tasks)
        for resp in responses:
            print(f"Request to {resp.url} ended with status: {resp.status_code}")
    total_end = time.perf_counter()
    print(f"Total Async Time: {total_end - total_start:.4f}s")

test_sync()
print()
asyncio.run(test_async())

#без асинхронного view у Sync був час 0.15, Async 0.18
