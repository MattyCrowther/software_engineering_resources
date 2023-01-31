class LoggingContextManager:

	'''
	called before entering with-statement body
	return value bound to as variable
	can return value of any type
	commonly returns context-manager itself
	'''
	def __enter__(self):
		print('LoggingContextManager.__enter__()')
		return 'You are in a with-block'
	'''
	exc_type = exception type
	exc_val = exception object
	exc_tb = exception traceback
	above are set to None if no exception thrown
	__exit__ re-raises the exception if returns false so dont re-raise exceptions yourself unless its the __exit__ that fails itself.
	'''
	def __exit__(self,exc_type,exc_val,exc_tb):
		if exc_type is None:
			print('LoggingContextManager.__exit__: normal exit detected')
		else:
			print('LoggingContextManager.__exit__: Exception detected (type={},value={},traceback={})'.format(exc_type,exc_val,exc_tb))
		return


def main():
	with LoggingContextManager() as x:
		print(x)
	print("\n\n")
	with LoggingContextManager() as x:
		raise ValueError('Something has gone wrong!')

if __name__ == "__main__": main()