class Base:
	def __init__(self):
		print('Base initialiser')

	def f(self):
		print('Base.f()')

class Sub(base):
	def __init__(self):
		super.__init__() #Unlike many other languages sub classes do not automatically call base class initialiser so must do it manually in py
		print('Sub initialiser')

	def f(self):
		print('sub.f()')