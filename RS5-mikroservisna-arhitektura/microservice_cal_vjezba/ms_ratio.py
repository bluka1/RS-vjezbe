import aiohttp
from aiohttp import web

app = web.Application()

async def handle_ratio(request):
  data = await request.json()
  podaci = data.get('podaci')
  zbroj = data.get('zbroj')
  d = [round(i / zbroj, 2) for i in podaci]
  return web.json_response({"ratio_list": d})

app.router.add_post('/ratio', handle_ratio)

web.run_app(app, host='localhost', port=8082)
