


import queue  
lifo = queue.LifoQueue()

lifo.put('First-process')
lifo.put('Second-process')
lifo.put('Third-process')

for i in range(3):
    print(lifo.get())

