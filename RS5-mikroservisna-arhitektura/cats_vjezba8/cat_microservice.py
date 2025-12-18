from aiohttp import web
import aiohttp

app = web.Application()
API_URL = 'https://catfact.ninja/facts'

async def get_facts(req):
  async with aiohttp.ClientSession() as session:
    res = await session.get(API_URL)
    data = await res.json()
    return web.json_response(data)
  
async def get_num_facts(req):
  amount = req.match_info.get('amount')
  async with aiohttp.ClientSession() as session:
    res = await session.get(f'{API_URL}?limit={amount}')
    data = await res.json()
    return web.json_response(data)

app.router.add_get('/cats', get_facts)
app.router.add_get('/cat/{amount}', get_num_facts)

web.run_app(app, port=8086)
