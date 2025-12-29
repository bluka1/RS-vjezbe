from aiohttp import web


async def handle_squares(req):
  data = await req.json()
  podaci = data.get('podaci')
  kvadrati = [i ** 2 for i in podaci]
  return web.json_response({'kvadrati': kvadrati})

app = web.Application()
app.router.add_post('/kvadrati', handle_squares)

web.run_app(app, host='localhost', port=8083)
