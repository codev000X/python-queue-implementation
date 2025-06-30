class Queue:
    def __init__(self):
        self.item = []
    
    def __str__(self):
        values = [str(x) for x in self.item]
        return " ".join(values)
    
    def isEmpty(self):
        if self.item == []:
            return True
        return False
    
    def enqueue(self , value):
        self.item.append(value)
        return 'Successfully addded .'
    
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is Empty .'
        self.item.pop(0)
        