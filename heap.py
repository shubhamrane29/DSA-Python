#Heapq follows minimum heap
import heapq
heap = [17,90,56]

#Push the item maintaing the heap property
heapq.heappush(heap,10)
heapq.heappush(heap,1)
heapq.heappush(heap,5)
print('Push:',heap)

#Delete and return the smallest value
heapq.heappop(heap)
print('Pop:',heap)

#Convert list to heap
list1 = [1,3,4,7,9,10,2]
heapq.heapify(list1)
print('Heapify:',list1)

#Push the item and then delete and return the smallest value
heapq.heappushpop(heap, 7)
print('Push Pop:',heap)

#First pop then insert
heapq.heapreplace(heap, 23)
print('Replace:',heap)

#gives n smallest number
print('Smallest:', heapq.nsmallest(2, heap))

#gives n largest number
print('Largest:', heapq.nlargest(3, heap))

#Priority Queue
list2 = [(1, 'red'), (4, 'green'), (3, 'blue')]
for i in range(len(list2)):
    print(heapq.heappop(list2))