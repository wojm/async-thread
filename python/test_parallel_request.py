# global
import time
import requests
import asyncio
import pytest

# local
from async_request import async_get


def test_server_exists():
	requests.get('http://localhost:5000')


def test_server_sleeps_1_second():
	start = time.time()
	requests.get('http://localhost:5000/sleep/1')
	end = time.time()
	elapsed = end - start
	assert 0.9 < elapsed < 1.1, f'time elapsed: {elapsed}'


def test_synchronous_sleeps():
	start = time.time()
	requests.get('http://localhost:5000/sleep/1')
	mid = time.time()
	elapsed = mid - start
	assert 0.9 < elapsed < 1.1, f'time elapsed: {elapsed}'
	requests.get('http://localhost:5000/sleep/2')
	end = time.time()
	elapsed2 = end - start
	assert 2.9 < elapsed2 < 3.1, f'time elapsed: {elapsed2}'


@pytest.mark.asyncio
async def test_parralel_sleeps():
	start = time.time()
	promise1 = async_get('http://localhost:5000/sleep/1')
	promise2 = async_get('http://localhost:5000/sleep/2')
	mid = time.time()
	assert mid - start < 0.1
	gathered = await asyncio.gather(promise1, promise2)
	end = time.time()
	elapsed = end - start
	assert 1.9 < elapsed < 2.1, f'time elapsed: {elapsed}'
	assert len(gathered) == 2, 'two results are returned'
	assert gathered[0] == 'slept 1 seconds'
	assert gathered[1] == 'slept 2 seconds'
