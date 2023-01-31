
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__, self.x, self.y)

#Note can use these but better using get has del set attr.
def main():
	v = Vector(5,3)
	print(v)
	print(dir(v))
	print(v.__dict__)
	print(type(v.__dict__))
	print(v.__dict__['x'])
	v.__dict__['x'] = 17
	print(v.x)
	#del v.__dict__['x']
	y = 'x' in v.__dict__
	print(y)

if __name__ == "__main__": main()