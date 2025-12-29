from aiohttp import web

app = web.Application()
async def handle_square_roots(req):
  data = await req.json()
  podaci = data.get('podaci')
  korijeni = [i ** 0.5 for i in podaci]
  return web.json_response({'korijeni': korijeni})

app.router.add_post('/korijeni', handle_square_roots)

web.run_app(app, host='localhost', port=8084)
