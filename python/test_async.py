# global
import time
import timeit
import pytest
import asyncio

# local
from my_sleep import synchronous_sleep, asynchronous_sleep


def test_pytest():
	assert True, 'pytest works'

def test_sleep_5():
	start = time.time()
	synchronous_sleep(1)
	end = time.time()
	assert 0.9 < end - start < 1.1, f'sleeps at least 0.9, waited {end - start}'
	assert type((end - start)) == float
	

def test_sleep_alt():
	time_elapsed = timeit.timeit('from my_sleep import synchronous_sleep \nsynchronous_sleep(1)', number=1)
	assert (0.9 < time_elapsed < 1.1) , 'time elapsed less than 0.9s or greater than 1.1s'


def test_async_sleep_5():
	start = time.time()
	asynchronous_sleep(1)
	mid = time.time()
	assert mid - start < 0.1, f'without awaiting the syncronous sleep, we proceed right away, took: {mid - start}'
	print(mid - start)


@pytest.mark.asyncio
async def test_async_sleep_5():
	start = time.time()
	promise = asynchronous_sleep(1) # add to event loop
	print('do stuff')
	await promise  # synchronous_sleep()

	end = time.time()
	assert 0.9 < (end - start) < 1.1, f'with awaiting the asyncronous sleep took between 0.9 and 1.1s, took {end - start}'
	print(end - start)

@pytest.mark.asyncio
async def test_two_sleeps():
	start = time.time()
	await asyncio.gather(
		asynchronous_sleep(1),
		asynchronous_sleep(2),
	)
	end = time.time()
	assert 1.9 < end - start < 2.1, f'parallel async functions take 2 seconds, took {end - start}'

