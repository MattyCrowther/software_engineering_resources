def main():
	v = 0b11110000
	print(v)
	print(~v) #bitwise NOT op
	print(bin(~v)) 
	print(~0b11110000 & 0b11111111)
	print(bin(~0b11110000 & 0b11111111))
	print(int(32).bit_length())
	print(int(240).bit_length())
	print(int(256).bit_length())

if __name__ == "__main__":main()