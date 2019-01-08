class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
        

x = MyClass()        

if __name__ == "__main__":
	print x.i
	print x.__doc__
	x.i = 20
	print x.i
