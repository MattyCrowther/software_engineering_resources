'''
This is NOT a class decorator but an instance of a class decorator, this means that the decorator will function given the state of the given object.
For example the Trace class has a bool which can enable or disable tracting on a function call.
'''
class Trace:
	def __init__(self):
		self.enabled = True

	def __call__(self,f):
		def wrap(*args,**kwargs):
			if self.enabled:
				print('Calling {}'.format(f))
			return f(*args,**kwargs)
		return wrap

tracer = Trace()

@tracer
def rotate_list(l):
	return l[1:] + [l[0]] # l[1:] means from 1 to end