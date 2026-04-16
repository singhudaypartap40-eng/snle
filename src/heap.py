class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, i):
        while i > 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        self.swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()
        self._bubble_down(0)
        return min_item

    def _bubble_down(self, i):
        smallest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left

        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self._bubble_down(smallest)

    def is_empty(self):
        return len(self.heap) == 0