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

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self ,value):
        new_node = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = self.linkedList.tail =new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node