#else in a for loop only occurs when the item in the for loop is empty (Never runs.)
def ensure_has_divisible_worse(items,divisor):
	for item in items:
	    if item % divisor == 0:
	        found = item
	        break
	else:  # nobreak
	    items.append(divisor)
	    found = divisor

	print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))

def ensure_has_divisible_better(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    items.append(divisor)
    return divisor

#better is an alternative way that does the same thing but is more readable.
def main():
	items = [2, 25, 9, 37, 24, 28, 14]
	divisor = 12
	ensure_has_divisible_worse(items,divisor)
	ensure_has_divisible_better(items,divisor)

if __name__ == "__main__":main()
