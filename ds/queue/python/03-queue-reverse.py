from queue import Queue
import copy


def reverseQueue(queue: Queue):
    if queue.empty():
        return
    
    item = queue.get()
    reverseQueue(queue)
    queue.put(item)

def displayQueue(queue: Queue):
    while(not queue.empty()):
        print(queue.get())


q = Queue()
tem = Queue()

q.put(10)
q.put(20)
q.put(30)
q.put(40)

reverseQueue(q)
tem.queue = copy.deepcopy(q.queue)
displayQueue(tem)

reverseQueue(q)
tem.queue = copy.deepcopy(q.queue)
displayQueue(tem)
