from pprint import pprint as pp
import inspect

def report_scope(arg):
	x = 496
	pp(locals(),width = 10)

def main():
	i = 7
	print(type(i))           			   #int
	print(int)               			   #int
	print(repr(int))		 			   #int
	print(type(i) is int)    			   #True
	print(type(i)(78))       			   #78
	print(type(type(i)))     			   #type
	print(i.__class__)       			   #int
	print(i.__class__.__class__)    	   #type
	print(i.__class__.__class__.__class__) #type (Confirms type is its own type)

	print(issubclass(type,object))         #True
	print(type(object))                    #type (This and above shows circulary dependancy)

	print(isinstance(i,int))			   #True

	print(dir(i))						   #shows all attributes and method names



	print("\n\n")
	print(globals())        #The globals() method returns the dictionary of the current global symbol table.           
	a = 42
	globals()['a'] = 25
	print(globals())        #See here my variable is set as a global
	print("\n")
	print(locals())         #i = 7 a = 42  
	print(report_scope(42)) #Shows local scope of values.


	print("\n\n")
	print(inspect.ismodule(inspect)) 				   #the function returns if the param is a module or not
	print(inspect.getmembers(inspect,inspect.isclass)) #Search for memeber functions/vars etc optional param to refine, eg here specifically for isclass.


if __name__ == "__main__":main()
