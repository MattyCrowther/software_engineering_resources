'''
How to raise a different exception when one is caught.
Also shows how to use the traceback module for debugging
'''
import math
import traceback

class InclinationError(exception):
	pass

def inclination(dx,dy):
	try:
		return math.degrees(math.atan(dy / dx))
	except ZeroDivisionError as e:
		raise InclinationError("Slop cannot be vertical") from e

def main():
	try:
		inclination(0,5)
	except InclinationError as e:
		print(e.__traceback__)
		traceback.print_tb(e.__traceback__)
		s = traceback.format_tb(e.__traceback__)
		print(s)

if __name__ == '__main__':
	main()
	print("Finished")