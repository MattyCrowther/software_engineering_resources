'''
Example to show how we can deal with exceptions such as when the input is an empty set. See lines 18 + 19 and also 7
'''
def median (iterable):

	items = sorted(iterable)
	if len(items) == 0:
		raise ValueError("median() arg is an empty sequence")
	median_index = (len(items) - 1) // 2
	if len(items) % 2 != 0:
		return items[median_index]
	return (items[median_index] + items[median_index + 1]) / 2.0

def main():
	try:
		median([])
	except ValueError as e:
		print("Payload:" , e.args)
		print(str(e))

if __name__ == '__main__' : 
	main()