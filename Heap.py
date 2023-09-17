import time

class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, indx):
        return ((indx+1)//2 - 1) # +1 -1 because I'm working with indexes not positions
    
    def left_child(self, indx):
        return ((indx+1)*2 - 1)
    
    def right_child(self, indx):
        return ((indx+1)*2+1) - 1
    
    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def insert(self, item):
        self.heap.append(item)
        indx = len(self.heap) - 1
        while self.parent(indx) >= 0:
            if self.heap[indx] < self.heap[self.parent(indx)]:
                self.swap(indx, self.parent(indx))
                indx = self.parent(indx)
            else:
                break

    def remove(self):
        popped = self.heap[0]
        self.swap(0, len(self.heap) - 1)
        self.heap.pop(len(self.heap) - 1)
        indx = 0

        while self.right_child(indx) <= (len(self.heap) - 1):
            if self.heap[self.right_child(indx)] > self.heap[indx] and self.heap[self.left_child(indx)] > self.heap[indx]:
                break
            elif self.heap[self.right_child(indx)] < self.heap[indx] or self.heap[self.left_child(indx)] < self.heap[indx]:
                if self.heap[self.right_child(indx)] <= self.heap[self.left_child(indx)]:
                    self.swap(indx, self.right_child(indx))
                    indx = self.right_child(indx)
                else:
                    self.swap(indx, self.left_child(indx))
                    indx = self.left_child(indx)

        if self.left_child(indx) == (len(self.heap) - 1) and self.heap[self.left_child(indx)] < self.heap[indx]:
            self.swap(indx, self.left_child(indx))
        
        return popped



from random import randint
from time import perf_counter
import matplotlib.pyplot as plt

length = 2
heap_graph = []
sort_graph = []
xcord = []
for i in range(5000):
    random_list = []
    for i in range(length):
        random_list.append(randint(0, 5000))
    returned = 1 # len(random_list)

    #Heap
    start = perf_counter()
    heap = Heap()

    for x in random_list:
        heap.insert(x)
    heap_list = []
    for i in range(returned):
        rm = heap.remove()
        if rm != None:
            heap_list.append(rm)

    end = perf_counter()
    heap_time = end-start

    #Sort
    start = perf_counter()
    sorted_ = sorted(random_list)
    sort_list = []
    for i in range(returned):
        if len(sorted_) > 0:
            sort_list.append(sorted_[0])
            sorted_.pop(0)
    end = perf_counter()
    sort_time = end-start

    if heap_list == sort_list:
        print("Lists match,", length)
        xcord.append(length)
        length += 1

        heap_graph.append(heap_time)
        sort_graph.append(sort_time)
    else:
        print("Error: the two lists don't match")
        print(random_list)
        print(heap_list)
        print(sort_list, "\n")
        break

print(f"Heap average:{sum(heap_graph)/len(heap_graph)}")
print(f"Sort average:{sum(sort_graph)/len(sort_graph)}")
print(f"Sort is {(sum(heap_graph)/len(heap_graph))/(sum(sort_graph)/len(sort_graph))} faster")

plt.plot(xcord, heap_graph, label="heap")
plt.plot(xcord, sort_graph, label="sort")
plt.legend()
plt.show()
