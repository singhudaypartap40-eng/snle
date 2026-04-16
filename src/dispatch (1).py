from heap import MaxHeap

class DispatchQueue:
    def __init__(self):
        self.heap = MaxHeap()

    def enqueue(self, package):
        self.heap.insert((package.priority, package))

    def dequeue(self):
        item = self.heap.extract_max()
        if item:
            return item[1]
        return None

    def peek(self):
        item = self.heap.peek()
        if item:
            return item[1]
        return None

    def is_empty(self):
        return self.heap.is_empty()