'''
Global Points.
	 Can call a static method (in python this is a module function, remember modules != classes), to do this its like **name_of_file**.function_call()
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
 __init__ is like a constructor for an object it is called as soon as an object is created.
 __call__ is called whenever the object is called after creation. It is like instead of inputing object.function() you type object() this calls this func.
 Example of a object which keeps information from previous calls (cache system)
 Everything in python is an object.
 constructor calls are made by calling the class object (Can check if something is callable by using callable(obj_etc) will show if its callable or not (Most things are))
'''
from pprint import pprint as pp
import socket
class Resolver:
	def __init__(self):
		self._cache={}

	def __call__(self,host):
		if host not in self._cache : 
			self._cache[host] = socket.gethostbyname(host)
		return self._cache[host]

	def clear(self):
		self._cache.clear()

	def has_host(self,host):
		if host in self._cache :
			return True
		else : 
			return False

#Summarize:
'''
	Function can be generalised into the notion of callables, we can make callable objects from instances, 
	we can make callable objects from instances by implementing the __call__ method, we can then invoke the object as if it was a function, 
	we can use this to define a function which maintain state such as caches.
'''
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is just a conditional expression that can be used in python, basically is: TRUE_value if condition else FALSE_value
def sequence_class(isImmutable):
	return tuple if isImmutable else list
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def sorted_by_surname(names):
	#Uses lambda which allows for creation of anonymous functions (no name) at runtime, stops from requiring all the typing overhead. The full equivalent is below.
	sorted(names,key=lambda name: name.split()[-1])
	return sorted

def lambda_explanation(name):
	return name.split()[0]

'''
 Rules for lambda:
 	Body is a single expression
 	No return value is needed or allowed.
 	Argument list terminated by a colon seperated by commas.
'''
'''
Summarize:
	A single expression can be used as a callable by creating a lambda which is an annoymous callable, most freq used directly as arguments to other functions.
	Like other functions the lambda argument list isnt enclosed in parenthasis and the lambda body is constricted to be a single expression the value will be returned.
'''
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This function is to teach about the *lengths, this allows for n number of arguments to be passed as parameters eg hypervolume() will throw excetion due to now
#having any args but hypervolume(1,2,3) and hypervolume(1,2) are valid.
def hypervolume(length,*lengths):
	v = length
	for item in lengths :
		v *= length
	return v

#kwargs (**kwargs) is like *args but for key words arguments ie named arguments such as resolver.tag('not_kwarg', kwarg1=1,hello="hello")
# It is simply arguments passed by keyword n number of times.
def tag (name,**attributes):
	result = '<' + name
	for key, value in attributes.items():
		result += ' {k}="{v}"'.format(k=key,v=str(value))
	result += '>'
	return result

#This shows how the above functions can be called with lists and tuples to populate the args and kwargs arguments.
def Extended_actual_arg_example(listt,tuplee):
	hypervolume(1,*list)
	tag('img',**tuple)

#Bit of a weird one this, try it call: trace(int,"ff",base=16) basically calls the first argument with the args and kwargs
def trace(f,*args,**kwargs):
	print("args = ",args)
	print("kwargs = ", kwargs)
	result = f(*args,**kwargs)
	print("Result =", result)
	return result

#Transposition basically inverts the list of lists so the columns become the rows and visa-versa
def transposition_example():
	sunday = [12,14,15,16,17,12,32,12,23,12,32]
	monday = [12,34,12,23,12,45,12,23,19,17,16]
	tuesday = [1,2,3,4,5,6,7,8,9,0,11]

	print("List of Lists:")
	daily = [sunday,monday,tuesday]
	pp(daily)

	#for item in zip(*daily):
		#print(item)

	#This is the same as commented out code above but is a better way of doing.
	#The *daily is taking a list of n lists and zipping then passes result of zip to list constructor
	print("-----------------------------")
	print("Transposed List of lists")
	transposed = list(zip(*daily))
	pp(transposed)



#Some extra rules about *args and **kwargs
	#Can rename args and kwargs to anything just need * for args and ** for keyword args
	#If using *args and **kwargs must have them in this orger (args first then kwargs second)
	#Any arguments preceding args of kwargs are seperate and will not be inside args + any after must be given as mandatory keyword args


'''
Summarize:
	Extended Argument Syntax allows arbitary positional arguments to be accepted using the *args syntax in the callable definition which results in arguments being 
	packaged into a tuple.
	Arbitary keyword agurments can be acceped by using **kwargs which results in keyword args being packaged into a dictionary, 
	extended call syntax allows us to unpack iterable series and mappings into positional and keyword function arguments respectiley.
	There is  no need to use * and ** at callside to correspond to the definition. Can also be used with normal arguments and keyword arguments.
'''
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------




