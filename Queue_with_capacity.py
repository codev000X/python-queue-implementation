class Queue:
    def __init__(self , maxSize ):
        self.maxSize = maxSize
        self.item = maxSize * [None]
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.item]
        return " ".join(values)

    def isFull(self):
        if self.start == 0 and self.top+1 == self.maxSize:
            return True 
        
        elif self.top + 1 == self.start:
            return True
        
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def enqueue(self , value):
        if self.isFull():
            return "Queue reached it maximium size ."

        else:
            if self.top == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.item[self.top] = value
            return "Element added succesfully ."

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty ."
        else:
            firstElement = self.item[self.start]
            start = self.start
            if self.start == self.top:
                self.top = self.start = -1
            elif self.start == self.maxSize:
                self.start + 1 = 0
            else:
                self.start += 1

            self.item[start] = None
            return firstElement