'''
This script shows that functools is often needed to keep the meta information of a function etc.
When a decotrator is used on a function is takes the metadata of the decorator which is already needed.
This packages function does the commented code for you.
'''
import functools
def noop(f):
	@functools.wraps(f)
	def noop_wrapper():
		return f
	#noop_wrapper.__name__ = f.__name__   This is not needed now functools is used.
	#noop_wrapper.__doc__ = f.__doc__
	return noop_wrapper

@noop
def hello():
	print("Hello World")