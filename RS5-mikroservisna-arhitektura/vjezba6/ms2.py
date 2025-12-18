from aiohttp import web
import asyncio
app = web.Application()
async def get_pozdrav(req):
  await asyncio.sleep(4)
  return web.json_response({"message": "Pozdrav nakon 4 sekunde"}, status=200)

app.router.add_get('/pozdrav', get_pozdrav)

web.run_app(app, port=8082)
