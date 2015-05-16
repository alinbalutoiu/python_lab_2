# decoratori
'''
def my_decorator(functie):
	def wrapper():
		print 'Inainte de functie %s' % functie.func_name
		functie()
		print 'dupa functie %s' % functie.func_name

	return wrapper

def f():
	print 'Hello world din f'

def f1(a):
	print a

f1 = my_decorator(f1)
'''









'''
def my_decorator(functie):
	def wrapper(**kwargs):
		print 'Inainte de functie %s' % functie.func_name
		functie(**kwargs)	# ** for unpacking
		print 'dupa functie %s' % functie.func_name

	return wrapper

def f():
	print 'Hello world din f'

def f1(a):
	print a

f1 = my_decorator(f1)
'''









'''
def my_decorator(functie):
	def wrapper(*args, **kwargs):
		print 'Inainte de functie %s' % functie.func_name
		functie(*args, **kwargs)	# ** for unpacking
		print 'dupa functie %s' % functie.func_name

	return wrapper

def f():
	print 'Hello world din f'

def f1(a):
	print a

f1 = my_decorator(f1)
'''
'''
>>> from decorators import *
>>> f1(1)
Inainte de functie f1
1
dupa functie f1
>>> f1(a=1)
Inainte de functie f1
1
dupa functie f1
>>> f1(b=1)
Inainte de functie f1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "decorators.py", line 41, in wrapper
    functie(*args, **kwargs)	# ** for unpacking
TypeError: f1() got an unexpected keyword argument 'b'
>>> 
'''





import functools

def my_decorator(functie):
	@functools.wraps(functie)
	def wrapper(*args, **kwargs):
		print 'Inainte de functie %s' % functie.func_name
		functie(*args, **kwargs)	# ** for unpacking
		print 'dupa functie %s' % functie.func_name

	return wrapper

def f():
	print 'Hello world din f'

@my_decorator
def f1(a):
	print a
	raise Exception("my message")
#f1 = my_decorator(f1)

'''
def my_decorator(functie):
	def wrapper(*args, **kwargs):
		print 'Inainte de functie %s' % functie.func_name
		functie(*args, **kwargs)	# ** for unpacking
		print 'dupa functie %s' % functie.func_name

	return wrapper

def f():
	print 'Hello world din f'

def f1(a):
	print a

f1 = my_decorator(f1)
'''
