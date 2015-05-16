import threading

# _ -> considered to be private, just a convention

def apply_lock(func):
	def wrapper(inst, *args, **kwargs):
		with inst._lock:
			return func(inst, *args, **kwargs)
	return wrapper

class threadsafeDict(dict):
	_lock = threading.Lock()

	@apply_lock
	def __getitem__(self, key):
		#with self._lock:
		return super(threadsafeDict, self).__getitem__(key)

	@apply_lock
	def __setitem__(self, key, value):
		#with self._lock:
		return super(threadsafeDict, self).__setitem__(key, value)

'''
# context manager, nu trebuie sa dam close la fisier
with open ('nume_fisier', 'w') as f:
	f.write('tes')
'''

mydict = threadsafeDict()
mydict['test'] = 10
print mydict['test']