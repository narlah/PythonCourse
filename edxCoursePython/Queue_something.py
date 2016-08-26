class Queue(object):

    def __init__(self):
        self.vals = []

    def insert(self,element):
        self.vals.insert(0,element)

    def remove(self):
        if len(self.vals)==0:
            raise ValueError()
        else:
            return self.vals.pop(len(self.vals)-1)

queue = Queue()
queue.insert(5)
queue.insert(6)
print queue.remove()
queue.insert(7)
print queue.remove()
print queue.remove()
print queue.remove()