from aiohttp import web
import functools

app = web.Application()

async def get_umnozak(req):
  data = await req.json()
  if not isinstance(data, list) or not all([d for d in data if type(d) == 'int']):
    return web.json_response({'error': 'Dopustena je samo lista cijelih brojeva kao input'}, status=400)
  return web.json_response({'umnozak': functools.reduce(lambda x, y: x * y, data, 1)})

app.router.add_post('/umnozak', get_umnozak)
web.run_app(app, port=8084)
