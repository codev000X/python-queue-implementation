from multiprocessing import Queue

customQueue = Queue(maxsize=3)
customQueue.put(1)
customQueue.put(2)

print(customQueue.qsize())


# The multiprocessing module has same methods as the Queue module except for the join and task_done methods .