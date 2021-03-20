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
Enqueue is one of the operations we can use in Queue. Is nothing but *inserting data into the queue*, specifically into the back of the queue.

If we take the example of the music streaming app. Every time we add a song to the list, it is basically doing an Enqueue process as the following images show:

![Queue](queue-enqueue.png)

# Dequeue
Dequeue is another operation that we can use in queues. Dequeue *deletes data or items from the Queue*, specifically deleting from the front of the Queue.

Taking the example. We can see that the first item is playing right now and then when this process is finished the song is dequeue. It is to say, this first element is removed from the list. 

![Queue](queue-dequeue.png)
# Example
# Problem to Solve

