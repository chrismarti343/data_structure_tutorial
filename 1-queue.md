# Queue
# Introduction
The term Queue is use to modified a group of items stored in a list. You can basically can control the flow of your task using queues. In the real world queue is used to know the sequence of of people waiting their turn to be attended.

The most used type of queues are the following:
- FIFO
- LIFO
  
# FIFO rule
FIFO stand for first in, first out. Basically FIFO gets the first item that first was put in.

A common problem of using FIFO we can find is in the music streaming apps. When we add a song to our list and then we play the list, the app will play from the first songs to the last one in th list.                              

```python
import queue

q = queue.Queue()

songs = ['First-song', 'Second-song', 'Third-song', 'Fourth-song']

for i in songs:
    q.put(i)
    print(q.get())
```

As result of this example we have the following:

christ




# LIFO rule
# Enqueue
# Dequeue
# Example
# Problem to Solve

