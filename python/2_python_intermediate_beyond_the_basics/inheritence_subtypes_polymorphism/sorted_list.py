class SimpleList:
	def __init__(self,items):
		self._items = list(items)

	def add(self,item):
		self._items.append(item)

	def __getitem__(self,index):
		return self._items[index]

	def sort(self):
		self._items.sort()
	
	def __len__(self):
		return len(self._items)
	
	def __repr__(self):
		return "SimplifiedList({!r})".format(self._items)


class SortedList(SimpleList):
	def __init__(self,items=()):
		super().__init__(items)
		self.sort()

	def add(self,item):
		super().add(item)
		self.sort()
	
	def __repr__(self):
		return "SortedList({!r})".format(list(self))

class IntList(SimpleList):
	def __init__(self,items=()):
		for x in items: self._validate(x)
		super().__init__(items)
	
	@staticmethod
	def _validate(x):
		if not isinstance(x,int):
			raise TypeError('intList only supports in values.')	

	def add(self,item):
		self._validate(item)
		super().add(item)
	
	def __repr__(self):
		return "IntList({!r})".format(list(self))

#Can call SortedIntList._mro_ to find out the Method Resolution Order ie where is searched and in which order for calls. (Walks along the inhertience.) In this case it is SortedIntList IntList SortedList SimpleList Object
#Why does calling add on sortedIntList keep the constraint of SortedList and IntList with the info above?
	#Because add() calls super. When SortedIntList.add() is called it calls IntList.add() which calls super().add which you would think would call SimpleList.add() but because of MRO it calls the above in the heirachy which 
	#happens to be SortedList.add()
def SortedIntList(SortedList,IntList):
	def __repr__(self):
		return 'SortedIntList({!r})'.format(list(self))