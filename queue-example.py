
'''
CSE212
(c) BYU-Idaho
01-Queue - Example 1
Coronavirus vaccination list
'''

class vaccination_Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self,name):
        self.queue.append(name)

    def dequeue(self):
        if len(self.queue) <= 0:
            raise IndexError()

        name = self.queue[0]
        del self.queue[0]
        return name

    def get_queue(self):
        return self.queue


print('Test 1')
queue = vaccination_Queue()
queue.enqueue('Christian')
queue.enqueue('David')
queue.enqueue('Daniel')
queue.enqueue('Oscar')
print(queue.get_queue())
name = queue.dequeue()
print(queue.get_queue())
