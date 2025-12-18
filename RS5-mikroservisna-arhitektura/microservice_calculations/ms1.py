from aiohttp import web

app = web.Application()

async def get_zbroj(req):
  data = await req.json()
  # print('data:', data)
  # print('type data:', isinstance(data, list))
  if not isinstance(data, list) or not all([d for d in data if type(d) == 'int']):
    return web.json_response({'error': 'Dopustena je samo lista cijelih brojeva kao input'}, status=400)
  return web.json_response({'zbroj': sum(data)}, status=200)

app.router.add_post('/zbroj', get_zbroj)

web.run_app(app, port=8083)
