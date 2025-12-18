from aiohttp import web

app = web.Application()

async def get_kolicnik(req):
  try:
    data = await req.json()
    umnozak = int(data['umnozak'])
    zbroj = int(data['zbroj'])
    if zbroj == 0 or not isinstance(zbroj, int) or not isinstance(umnozak, int):
      return web.json_response({'error': 'Oba proslijedena broja moraju biti cijeli brojevi i zbroj ne smije biti 0. Dijeljenje s nulom nije dozvoljeno.'}, status=400)
    return web.json_response({'kolicnik': round(umnozak / zbroj, 2)}, status=200)
  except Exception as e:
    print('greska')
    return web.json_response({'error': 'Nesto je poslo po zlu.'})

app.router.add_post('/kolicnik', get_kolicnik)
web.run_app(app, port=8085)
