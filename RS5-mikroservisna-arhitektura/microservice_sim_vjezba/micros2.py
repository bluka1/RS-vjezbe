from aiohttp import web
import asyncio

async def poz(request):
  await asyncio.sleep(2)
  return web.json_response('Hello from microservice2')

app = web.Application()
app.router.add_get('/', poz)

if __name__ == '__main__':
  web.run_app(app, port=8082)
