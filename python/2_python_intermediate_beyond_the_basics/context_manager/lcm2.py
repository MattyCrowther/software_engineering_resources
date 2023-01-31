import contextlib
import sys
'''
Uses the contextlib decorator to handle context managers for us, means dont have to create a full class just a func
However we must re-raise the exception using this see raise line 16
'''

@contextlib.contextmanager
def logging_context_manager():
	print('logging_context_manager: enter()')
	try: 
		yield 'You are in a with-block!'
		print('Logging_context_manager: normal exit')
	except Exception:
		print('logging_context_manager: exceptional exit',sys.exc_info())
		raise

def main():
	with logging_context_manager() as x:
		raise ValueError('Something went Wrong!')

if __name__ == "__main__": main()