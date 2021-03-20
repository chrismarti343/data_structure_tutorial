# Queue
## Introduction
The term Queue is use to modified a group of items stored in a list. You can basically can control the flow of your task using queues. In the real world queue is used to know the sequence of of people waiting their turn to be attended.

The most used type of queues are the following:
- FIFO
- LIFO
  
# FIFO rule
FIFO stands for first in, first out. Basically FIFO gets the first item that first was put in.

A common problem of using FIFO we can find is in the music streaming apps. When we add a song to our list and then we play the list, the app will play from the first songs to the last one in th list.                              

```python
import queue

q = queue.Queue()

q.put('First-process')
q.put('Second-process')
q.put('Third-process')

for i in range(3):
    print(q.get())
```

As result of this example we have the following:

```bash
First-song
Second-song
Third-song
```

# LIFO rule
LIFO stands last in, first out. In this methods the last item in the list is the first item to be precessed, and the first element would be processes at the end.       

A common problem we find in the real world is when whe are using our computer. When the user waht to redo a proccess they re basically using LIFO method. The next emple shows how this process is perfomed:

```python
import queue  

lifo = queue.LifoQueue()

lifo.put('First-process')
lifo.put('Second-process')
lifo.put('Third-process')

for i in range(3):
    print(lifo.get())
```
As the result of this example we have the following:
```bash
First-process
Second-process
Third-process
```
# Enqueue
Enqueue is one of the operations we can use in Qqueue ueues. Is nothing but inserting data in to the queue, specificaly in to the back of the queue

# Dequeue
DEqueue is another operation that we can use in queues. Dequeue is delete data or item from the Queue, scepificaly deliting from the front of the Queue.
# Example
# Problem to Solve

