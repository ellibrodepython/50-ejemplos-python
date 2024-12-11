# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install aiohttp asyncio
# 2. Ejecuta el script: python 32_programacion_asincrona.py

import asyncio
import aiohttp

url_base = "https://api.github.com/users/{}"
usuarios = ["python", "google", "firebase"]

async def get_seguidores(session, usuario):
    url = url_base.format(usuario)
    async with session.get(url) as r:
        return usuario, int((await r.json())["followers"])

async def get_todos(usuarios):
    async with aiohttp.ClientSession() as s:
        tasks = [get_seguidores(s, u) for u in usuarios]
        return await asyncio.gather(*tasks)

r = asyncio.run(get_todos(usuarios))
for usuario, rr in r:
    print(f"Followers de {usuario}: {rr}")