class MyClass(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_method(self):
    	print self.a, self.b

class MyClassExtended(MyClass):
    def __init__(self, a, b, c):
        super(MyClassExtended, self).__init__(a, b)
            self.c = c

    def my_method(self):
        super(MyClassExtended, self).my_method()
        print self.c



# if we use only "import first_class" without "from first_class import *"
# obj = first_class.MyClass(1,2)
