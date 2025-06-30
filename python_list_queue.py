class Queue:
    def __init__(self):
        self.item = []
    
    def __str__(self):
        values = [str(x) for x in self.item]
        return " ".join(values)