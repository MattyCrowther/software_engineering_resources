'''
1.
	The next_serial is an iterator on instances of the class we need to use the . operator because otherwise next_serial cannot be found using the LEGB rule.
	Can't really just use self. either because although you can read you cannot write eg self.serial = self.next_serial will not work as it will create a new instance
	attribute which will hide the class definiton.

2. 
	Here we can see a staticmethod decorator used so the constructor can call this method independantly of instances of a class, A staticmethod is just a function defined inside a class. 
	It does not  know anything about the class or instance it was called on and only gets  the arguments that were passed without any implicit first argument.

3. classmethod recieves a class as the implicit first arugment where staticmethod has nothing (instance methods have self), this is useful to create factory methods
   as seen below we can create different objects without changing constructor definition.

4. We moved ShippingContainer to self. because if the subclass is called with default constructor then a instance of the base class is called. 
   If you was to call the static method an instance of subclass would be created.

 5.
 	Created the constructor for the derived class, super calls the base class constructor, however because we are calling base class methods they dont know about
 	celsius so we had to add *args and *kwargs for optional extras.

6.
	Python way of doing getter setter implementation, using special decorators we can make 
	class methods behave like attributes and write logic inside methods but assign like attributes.
	Also allows validation checking to come from one point.

'''
import iso6346
class ShippingContainer:

	HEIGHT_FT = 8.5
	WIDTH_FT = 8.0

	next_serial = 1337

	#2.
	@staticmethod
	def _get_next_serial():
		result = ShippingContainer.next_serial
		ShippingContainer.next_serial += 1
		return result

	#This just uses a external module to create a special code.
	@staticmethod
	def _make_bic_code(owner_code,serial):
		return iso6346.create(owner_code=owner_code,serial=str(serial).zfill(6))

	#3.
	@classmethod
	def get_next_serial(cls):
		result = cls.next_serial
		cls.next_serial += 1
		return result#
	#3	
	@classmethod
	def create_empty(cls,owner_code,length_ft,*agrs,**kwargs):
		return cls(owner_code,length_ft,contents=None,*agrs,**kwargs)
    #3
	@classmethod
	def create_with_items(cls,owner_code,items,*agrs,**kwargs):
		return cls(owner_code,length_ft,contents=list(items),*agrs,**kwargs)

	def __init__(self,owner_code,length_ft,contents):
		self.contents = contents
		self.length_ft = length_ft
		#this makes the code from a static function given the inputs from the params and modifiying using another static method.
		
		#.4
		#self.bic = ShippingContainer._make_bic_code(owner_code=owner_code,serial=ShippingContainer._get_next_serial())
		self.bic = self._make_bic_code(owner_code=owner_code,serial=ShippingContainer._get_next_serial()) 
		''' 1.
		self.serial = ShippingContainer.next_serial
		ShippingContainer.next_serial += 1
		'''

	@property
	def volume_ft3(self):
		return ShippingContainer.WIDTH_FT * ShippingContainer.HEIGHT_FT * self.length_ft

class RefrigeratedShippingContainer(ShippingContainer):

	MAX_CELSIUS = 4.0
	FRIDGE_VOLUME_FT3 = 100

    #.4	
	@staticmethod
	def _make_bic_code(owner_code,serial):
		return iso6346.create(owner_code=owner_code,serial=str(serial).zfill(6),category='R')

	#.6
	def _c_to_f(celsius):
		return celsius * 9/5 + 32

	#.6
	def _f_to_c(farenheit):
		return (farenheit - 32) * 5/9

	#.5
	def __init__(self,owner_code,length_ft,contents,celsius):
		super().__init__(owner_code,length_ft,contents)
		self.celsius = celsius #.6 Can now rely on celsius.setter to do max temp check.

	#.6
	@property
	def celsius(self):
		return self._celsius

	#.6
	@celsius.setter
	def celsius(self,value):
		if value > RefrigeratedShippingContainer.MAX_CELSIUS:
			raise ValueError("Temp too hot")
		self._celsius = value

	#.6
	@property
	def farenheit(self):
		return RefrigeratedShippingContainer._c_to_f(self.celsius)

	#.6
	@farenheit.setter
	def farenheit(self,value):
		self.celsius = RefrigeratedShippingContainer._f_to_c(value)

	#.7
	@property
	def volume_ft3(self):
		return (super.volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3)


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

	MIN_CELSIUS = -20.0

	@RefrigeratedShippingContainer.celsius.setter
	def celsius(self,value):
		if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS: 
			raise ValueError("Temp out of range")
		RefrigeratedShippingContainer.celsius.fset(self,value)
