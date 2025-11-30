# Zadatak 5: Pretvorba sinkronog koda u asinkroni
# Sljedeći isječak programskog koda pretvorite u asinkroni program s konkurentnom obradom mrežnih
# zahtjeva:**

# import requests

# def fetch_url(url: str) -> str:
#   response = requests.get(url, timeout=5)
#   return response.text

# def main():
#   urls = [
#     "https://example.com",
#     "https://httpbin.org/get",
#     "https://api.github.com"
#   ]

#   for url in urls:
#     content = fetch_url(url)
#   print(f"Fetched {len(content)} characters from {url}")

# if __name__ == "__main__":
#   main()

import aiohttp
import asyncio

async def fetch_url(url: str, session) -> str:
  response = await session.get(url, timeout=5)
  return await response.text()

async def main():
  urls = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://api.github.com"
  ]

  async with aiohttp.ClientSession() as session:
    tasks = []
    for url in urls:
      tasks.append(asyncio.create_task(fetch_url(url, session)))
    results = await asyncio.gather(*tasks)
    for url, result in zip(urls, results):
      print(f"Fetched {len(result)} characters from {url}")


asyncio.run(main())
