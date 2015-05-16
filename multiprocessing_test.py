import multiprocessing

myqueue = multiprocessing.Queue()

def count():
	for i in xrange(10):
		myqueue.put(i)

workers = []

for i in xrange(3):
	worker = multiprocessing.Process(target=count)
	#worker.setDaemon(True)		# sa se termine in acelasi timp cu aplicatia
	worker.start()
	workers.append(worker)

for worker in workers:
	worker.join()				# asteapta pana cand un anumit worker si-a terminat executia

while not myqueue.empty():
	print myqueue.get()

