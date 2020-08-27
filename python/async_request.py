import asyncio
import aiohttp

async def async_get(url):
	# make some anysnchronous request
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as resp:
			return await resp.text()
