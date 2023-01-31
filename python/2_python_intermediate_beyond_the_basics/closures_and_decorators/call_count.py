'''
This function is almost like a wrapper for a function, literally takes the function in (f) and keeps count of how many times it has been called.
'''
class CallCount:
	def __init__(self,f):
		self.f = f
		self.count = 0

	def __call__(self, *args, **kwargs):
		self.count +=1
		return self.f(*args,**kwargs)


#Simple function which actually uses a class as a decorator, hello(name) is passed to call count before its called, keeping the count.
@CallCount
def hello(name):
	print("Hello, {}".format(name))