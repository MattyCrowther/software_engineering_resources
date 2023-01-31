#Local Scope ------------------------------------------------------------------------------------------------------------------------------------------
#Negative index means you count from the right side instead of the left.
#Because functions are defined at runtime, last_letter() is redefined everytime sort_by_last_letter is called.
store = []
def sort_by_last_letter(strings):
	def last_letter(s):
		return s[-1]
	store.append(last_letter)
	print(last_letter)
	return sorted(strings,key=last_letter)

# LEGB is a rule which python follows to search for something: Local, then enclosing, then global, then built-in (Global in py means module level)
# outer() shows that the inner() function can get g,p and l 
# inner is only defined when outer is executed and even then its still not related so inner is not an attribute of outer.
g = 'global'
def outer(p='param'):
	l = 'local'
	def inner() : 
		print(g,p,l)
	inner()

#Can return function as seen below, comes back to the functions are first class idea, 
#So could do something like lf = enclosing_func()
#							lf()
def enclosing_func():
	def local_func():
		print('local_func')
	return local_func

#-------------------------------------------------------------------------------------------------------------------------------------------------

#Closures -------------------------------------------------------------------------------------------------------------------------------------------------
#Maintains a reference to objects from earlier scopes, even if the internal function is gone
#A way of thinking is that the local function closes over the object it needs to stop being garbage collected.

def enclosing():
	x = 'closed over'
	def local_func():
		print(x)
	return local_func

#lf = enclosing()
#lf()
#lf.__closure__ ##Note this checks if it is a closure, the closure act auto (if it needs to)
#This meants that lf is kept more specifically x.

#Function Factories - Functions that return other functions.
# python will create a closure to reference exp, as pow inside raise_to_exp uses it and is returned.
def raise_to(exp):
	def raise_to_exp(x):
		return pow(x,exp)
	return raise_to_exp
'''
#Can do something like
>>> square = module.raise_to(2)
>>> square.__closure__
(<cell at 0x7fcdd2a30588: int object at 0x7fcdd28bd9c0>,)
>>> square(5)
25
>>> square(9)
81
>>> cube = module.raise_to(3) 
>>> cube(2)
8
>>> cube(25)
15625

#This shows that the value exp can persist
'''

message = 'global'
def enclosing():
	message = 'enclosing'
	def local():
	   #global message ---- Note if this is added here then the final print would print 'local' ie the global variable
	   #non local message - Node if this is added here then the print after local() is called would print 'local' because 
	   #it allows message = 'local to live outside of the local function but not out of the enclosing scope' (syntax error when no enclosing)
		message = 'local'

	print('enclosing message: ',message)
	local()
	print('enclosing message: ',message)

print('global message: ',message) #prints global
enclosing()                       #prints enclosing + enclosing
print('global message: ',message) #prints global

#This above happens (local isnt printed even though message is set to this) because of scope, a new instance is made when the value is set.

import time
def make_timer():
		last_called = None

		def elapsed():
			nonlocal last_called
			now = time.time()
			if last_called is None :
				last_called = now
				return None
			result = now - last_called
			last_called = now
			return result

		return elapsed

#-------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------
#Decorators - Impletemented as callables take take callables and return other callables
#Allow it to be aple to modify existing code without changing existing function. (More maintainable)

#This is the decorator.
def escape_unicode(f):
	def wrap(*args,**kwargs): #-- We have seen this before just accepts any number of args or keyword args.
		x = f(*args,**kwargs) 
		print(x)
		return ascii(x)
	return wrap #Returns wrap because a decorator must always return a callable.

#Uses the decorator.
@escape_unicode
def northern_city():
	return "TromsØ"

'''
So what happens here:
	northern_city() is called.
	however a decorator is present.
	northern_city() gets passed as a param to escape_unicode(f) f == northern_city()
	x == return value of northern_city() (I think)
	returns all ascii values of x.
	returns function wrap.
'''




#-------------------------------------------------------------------------------------------------------------------------------------------------