import time
import timeit
from my_sleep import syncronous_sleep

def test_pytest():
	assert True, 'pytest works'

def test_sleep_5():
	start = time.time()
	syncronous_sleep(5)
	end = time.time()
	assert 4.9 < end - start < 5.1, f'sleeps at least 4.9, waited  {end - start}'
	assert type((end - start)) == float
	

def test_sleep_alt():
	time_elapsed = timeit.timeit('from my_sleep import syncronous_sleep \nsyncronous_sleep(5)', number=1)
	assert (4.9 < time_elapsed < 5.1) , 'time elapsed less than 4.9s or greater than 5.1s'
	
	# https://stackoverflow.com/questions/13628791/determine-whether-integer-is-between-two-other-integers
