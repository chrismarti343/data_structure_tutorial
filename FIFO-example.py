

import queue

q = queue.Queue()

songs = ['First-song', 'Second-song', 'Third-song', 'Fourth-song']

for i in songs:
    q.put(i)
    print(q.get())