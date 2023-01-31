'''
This class has its __str__ and __repr__ overridden to provide more useful information, classes should nearly always overide these.
Note: default impl of str is repr.

Can also call reprlib for using repr on lists.
'''
class Point2D:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	#str provides a more human readable format string. (str for user.)
	def __str__(self):
		return '({},{})'.format(self.x,self.y)

	#repr porives exactness over human-friendliness, includes identifying behaviour. (Useful for debugging/logging.) (repr for devs)
	def __repr__(self):
		return 'Point2D(x={},y={})'.format(self.x,self.y)


	#Converts to string i think, dont really need to use as python knows to just call __str__
	def __format__(self,f):
		if f == 'r':
			return '{},{}'.format(self.y,self.x)
		else:
			return '{},{}'.format(self.x,self.y)

    '''
    Not an overloaded method just shows you can change all non ascii values to ascii values.
    '''
	def string_to_ascii(string):
		return ascii(string)

	'''
	converts a value to its unicode value
	'''
	def ord(string):
		return ord(string)

	'''
	Converts a value from unicode back (Above is inverse)
	'''
	def chr(integer):
		return chr(integer)


