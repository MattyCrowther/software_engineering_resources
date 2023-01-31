'''
A metaclass is the class of a class. Like a class defines how an instance of the class behaves, a metaclass defines how a class behaves. A class is an instance of a metaclass.
meta classes give us the option to modify the dict of class attributes before the class is instantiated.

<- = more meta
mcs <- cls <- self

when to overide:
__prepare__ - When you want to customize the type or initial value of the namespace mapping
__new__     - When you want to allocate and optionally configue new class object
__init__    - Configure class object

mcs -metaclass
cls - class
'''
class TracingMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print("TracingMeta.__prepare__(name, bases, **kwargs)")
        print("  mcs =", mcs)
        print("  name =", name)
        print("  bases =", bases)
        print("  kwargs =", kwargs)
        namespace = super().__prepare__(name, bases)
        print("<-- namespace =", namespace)
        print()
        return namespace

    def __new__(mcs, name, bases, namespace, **kwargs):
        print("TracingMeta.__new__(mcs, name, bases, namespace, **kwargs)")
        print("  mcs =", mcs)
        print("  name =", name)
        print("  bases =", bases)
        print("  namespace =", namespace)
        print("  kwargs =", kwargs)
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        print("<-- cls =", cls)
        print()
        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
        print("TracingMeta.__init__(cls, name, bases, namespace, **kwargs)")
        print("  cls =", cls)
        print("  name =", name)
        print("  bases =", bases)
        print("  namespace =", namespace)
        print("  kwargs =", kwargs)
        super().__init__(name, bases, namespace)
        print()

    def metamethod(cls): #Instance method of meta class due to cls
        print("TracingMeta.metamethod(cls)")
        print("  cls = ", cls)
        print()

    def __call__(cls, *args, **kwargs):
        print("TracingMeta.__call__(cls, *args, **kwargs)")
        print("  cls =", cls)
        print("  args =", args)
        print("  kwargs =", kwargs)
        print("  About to call type.__call__()")
        obj = super().__call__(*args, **kwargs)
        print("  Returned from type.__call__()")
        print("<-- obj =", obj)
        print()
        return obj


class TracingClass(metaclass=TracingMeta):

    def __new__(cls, *args, **kwargs):
        print("  TracingClass.__new__(cls, args, kwargs")
        print("    cls =", cls)
        print("    args =", args)
        print("    kwargs =", kwargs)
        obj = super().__new__(cls)
        print("  <-- obj =", obj)
        print()
        return obj

    def __init__(self, *args, **kwargs):
        print("  TracingClass.__init__(self, *args, **kwargs")
        print("    self =", self)
        print("    args =", args)
        print("    kwargs =", kwargs)
        print()

class Widget(metaclass=TracingMeta):
        pass