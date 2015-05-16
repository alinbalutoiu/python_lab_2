import eventlet
eventlet.monkey_patch()

import time		# module by eventlet not by OS

def count():
	for i in xrange(10):
		print i

worker = eventlet.spawn(count)
time.sleep(0)
worker.wait()

