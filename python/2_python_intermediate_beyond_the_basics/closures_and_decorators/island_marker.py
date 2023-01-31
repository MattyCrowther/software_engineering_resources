'''
This shows how two decorators can be applied to a single function, note that it goes upwards, meanting escape_unciode is called before tracer
These examples have been talked through in other modules.
'''
def escape_unicode(f):
	def wrap(*args,**kwargs): #-- We have seen this before just accepts any number of args or keyword args.
		x = f(*args,**kwargs) 
		print(x)
		return ascii(x)
	return wrap #Returns wrap because a decorator must always return a callable.

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
@escape_unicode
def norwegian_island_marker(name):
	return name + "Øy"


####Extra######
#This is just an extra bit that shows that class methods can have decorators too.
class IslandMaker:
	def __init__(self,suffix):
		self.suffix = suffix

	@tracer
	def make_island(self,name):
		return name + self.suffix