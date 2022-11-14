import math

class Heap:
    def __init__(self, A, property_check = 0):
        self.property_check = property_check
        self.elements = []
        for e in A:
            self.insert(e)

    def getElements(self):
        return self.elements

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*(i + 1)

    def height(self):
        return math.floor(math.log(len(self.elements),2)) + 1

    def parent(self, i):
        return (i-1)//2 if i % 2 != 0 else (i//2 - 1)

    def buildMinHeapify(self):
        for i in range(len(self.elements)//2, -1, -1):
            self.minHeapify(i)

    def getRoot(self):
        return self.elements[0]

    def insert(self, e):
        self.elements.append(e)
        self.buildMinHeapify()

    def delete(self, key):
        self.elements.remove(key)
        self.buildMinHeapify()

    def update(self, old_key, new_key):
        self.delete(old_key)
        self.insert(new_key)

    def extract_min(self):
        self.update(self.getRoot(), self.elements[-1])
        self.elements.remove(97)

    def decrease_key(self, A, i, key):
        A[i] = key
        while i > 1 and self.parent(i) > A[i]:
            A[i], A[self.parent(i)] = A[self.parent(i)], A[i]
            i = self.parent(i)
        return A

    def minHeapify(self,root):
        left, right, largest = self.left(root), self.right(root), root
        if left < len(self.elements) and self.elements[root] > self.elements[left]:
            largest = left
        if right < len(self.elements) and self.elements[largest] > self.elements[right]:
            largest = right
        if largest != root:
            self.elements[largest], self.elements[root] = self.elements[root], self.elements[largest]
            self.minHeapify(largest)

    def __len__(self):
        return len(self.elements)

def main():
    A = Heap([20, 5, 4, 97, 1, 3, 8, 0])
    print(A.getElements())
    A.extract_min()
    print(A.getElements())
    lista = A.getElements()
    print(A.decrease_key(lista, 3, 6))
    A.insert(4)
    print(A.getElements())
main()