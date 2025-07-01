from collections import deque

# Creating the Queue.
customqueue = deque(maxlen = 3)
print(customqueue)

# Appending to Queue .
customqueue.append(1)
customqueue.append(2)
customqueue.append(3)
print(customqueue)

# If the length reaches to max then append method DoNot raise error but it overwrites the first element .
customqueue.append(4)
print(customqueue)

# Dequeuing via popleft() .
customqueue.popleft()
print(customqueue)

# Clearing the Queue via clear() .
customqueue.clear()
print(customqueue)