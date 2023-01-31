#---------------------------------------------------------------------------------------------
#Creates a set of points on a 5*3 matrix (Cartesian product)
#Way to think of this is nested for loop the y loop is nested inside each for loop of x.
print([(x,y) for x in range(5) for y in range(3)])

#This is the drawn out version of the above comprehension
points = []
for x in range(5):
	for y in range(3):
		points.append((x,y))
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
#Shows that you can have if statements etc nested.
values = [x / (x-y)
		 for x in range(100)
		 if x>50
		 for y in range(100)
		 if x - y !=0]

#Drawn out version of above comprehension
values = []
for x in range (100):
	if x>50:
		for y in range(100):
			if x - y != 0:
				values.append(x / (x-y))

#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
#Shows that variables defined previously can be used later (x)
[(x,y) for x in range(10) for y in range(x)]

#Same
result = []
for x in range(10):
	for y in range(x):
		result.append((x,y))
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
#EXTRA: Nested Compreshension
# Can use set comprehension inside another. 
#This will produce a list of lists, basically the x loop puts all the lists generated in the y loop.
vals = [[y*3 for y in range(x)] for x in range(10)]

outer = []
for x in range(10):
	inner = []
	for y in range(x):
		inner.append(y*3)
	outer.append(inner)

print(outer)

#---------------------------------------------------------------------------------------------
