from aiohttp import web
import aiohttp

app = web.Application()

async def check_fact(req):
  data = await req.json()
  facts = [obj['fact'] for obj in data['data']]
  valid_ones = [f for f in facts if 'cat' in f.lower() or 'cats' in f.lower()]
  return web.json_response(valid_ones, status=200)

app.router.add_post('/facts', check_fact)

web.run_app(app, port=8087)
