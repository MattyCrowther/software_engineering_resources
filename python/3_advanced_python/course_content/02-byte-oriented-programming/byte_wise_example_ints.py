import sys
def main():
	print(sys.byteorder)
	x = int(0xcafebabe).to_bytes(length=4,byteorder=sys.byteorder)
	print(x)
	y = int.from_bytes(x,byteorder=sys.byteorder)
	print(y)
	print(hex(y))
	

if __name__ == "__main__":main()