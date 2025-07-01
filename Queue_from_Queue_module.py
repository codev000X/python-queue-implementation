import queue as q

# Creating the queue_1 object from the Queue class .
queue_1 = q.Queue(maxsize=3)

# Using and Checking the empty method . 
print(queue_1.empty())

# Applying the put method .
queue_1.put(1)
queue_1.put(2)
queue_1.put(3)

# Checking the full method & empty method .
print(queue_1.full())
print(queue_1.empty())

# Checking the size of queue via qsize()
print(queue_1.qsize())

# Applying the get() method .
print(queue_1.get())

