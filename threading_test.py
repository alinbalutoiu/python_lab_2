import threading
from Queue import Queue

myevent = threading.Event
myevent.set()

myqueue = Queue()

def count():
	for i in xrange(10):
		myqueue.put(i)

workers = []

for i in xrange(3):
	worker = threading.Thread(target=count)
	worker.setDaemon(True)		# sa se termine in acelasi timp cu aplicatia
	worker.start()
	workers.append(worker)

for worker in workers:
	if worker != threading.current_thread:
		worker.join()				# asteapta pana cand un anumit worker si-a terminat executia

while not myqueue.empty():
	print myqueue.get()

