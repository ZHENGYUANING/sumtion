import time 
def countdown(n):
	while n > 0:
		print('t-ma',n)
		n -= 1
		time.sleep(1)

from threading import Thread 
t = Thread(target=countdown,args=(10,))
t.start()



