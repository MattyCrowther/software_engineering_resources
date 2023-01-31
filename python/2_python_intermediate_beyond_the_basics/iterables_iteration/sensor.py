#Fake sensor that had functionality to provide iter
#Iterates the incoming information as it comes.
import random
import datetime
import itertools
import time

class Sensor:
	def __iter__(self):
		return self
	
	def __next__(self):
		return random.random()

sensor = Sensor()
timestamps = iter(datetime.datetime.now,None) #None means it will go on forever, can add rule here to stop if item inside iter is met.

for stamp, value in itertools.islice(zip(timestamps,sensor),10):
	print(stamp,value)
	time.sleep(1)