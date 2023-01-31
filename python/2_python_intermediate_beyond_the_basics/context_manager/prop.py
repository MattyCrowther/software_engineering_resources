import contextlib

@contextlib.contextmanager
def propagater(name,propagate):
	try:
		yield
		print(name,'exited Normally')
	except Exception:
		print(name,'recieved an exception')
		if propagate:
			raise

def main():
	with propagater('outer',True),propagater('inner',False):
		raise TypeError('Cannot convert lead into gold')
	print("\n")
	with propagater('outer',False),propagater('inner',True):
		raise TypeError('Cannot convert lead into gold')
		
if __name__ == '__main__':main()
#Shows nested context managers, and that we can swallow exceptions, this can be done using method not using pre-defined decorator.