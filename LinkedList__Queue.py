class Node :
    def __init__(self , value = None):
        self.value = value
        self.next = None
    def __str__(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __iter__(self):
        curr = self.head
        while True:
            yield curr.value
            curr.next