import time
import asyncio

def synchronous_sleep(t):
	time.sleep(t)

async def asynchronous_sleep(t):
	print(f'a {t}')
	await asyncio.sleep(t)
	print(f'b {t}')
