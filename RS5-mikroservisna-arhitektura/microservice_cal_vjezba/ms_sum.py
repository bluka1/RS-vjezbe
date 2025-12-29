from aiohttp import web

async def handle_zbroj(request):
  data = await request.json()
  podaci = data.get('podaci')
  suma = sum(podaci)
  return web.json_response({"zbroj": suma})

app = web.Application()
app.router.add_post('/zbroj', handle_zbroj)
web.run_app(app, host='localhost', port=8081)
