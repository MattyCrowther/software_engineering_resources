'''
Implements __get__ __set__ and/or __delete__
'''
class DataDescriptor:

    def __get__(self, instance, owner):
        print("DataDescriptor.__get__({!r}, {!r}, {!r})"
              .format(self, instance, owner))

    def __set__(self, instance, value):
        print("DataDescriptor.__set__({!r}, {!r}, {!r})"
              .format(self, instance, value))

'''
Only impletments __get__
'''
class NonDataDescriptor:

    def __get__(self, instance, owner):
        print("NonDataDescriptor.__get__({!r}, {!r}, {!r})"
              .format(self, instance, owner))


class Owner:

    a = DataDescriptor()
    b = NonDataDescriptor()


def main():
  obj = Owner()

  #Data Descriptor
  print(obj.a)
  obj.__dict__['a'] = 196883
  print(obj.a)

  #Non-data descriptor
  print(obj.b)
  obj.__dict__['b'] = 744
  print(obj.b)


if __name__ == "__main__":main()