'''
This code makes a list of size n given the params.
For example if create_list("a",3) will return ["a","a","a"] etc.
The decorator stops the second arg from being a negative number.

The decorator is quite complex
	The validator inner function is the actual decorator as if takes the callable object and returns a callable object the
	the check_non_negative function is simply there to give the index position.

Note: also wrap forms a closure over index and f (the function)
'''


def check_non_negative(index):
	def validator(f):
		def wrap(*args):
			if args[index] < 0:
				raise ValueError("Argument {} must be non-negative." . format(index))
			return f(*args)
		return wrap
	return validator

@check_non_negative(1)
def create_list(value,size):
	return [value] * size