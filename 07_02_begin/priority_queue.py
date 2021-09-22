"""
Python Data Structures - A Game-Based Approach
Priority Queue Class based on heapq.
Robin Andrews - https://compucademy.net/
"""

import heapq


class PriorityQueue:
    
    def __init__(self):
        self.elements = []
        
    def put(self, item, priority):
        element = (priority, item)
        heapq.heappush(self.elements, element)
        
    def get(self):
        return heapq.heappop(self.elements)[1]
        
    def is_empty(self):
        return not self.elements
    
    def __str__(self):
        return str(self.elements)
    

if __name__ == "__main__":
    pq = PriorityQueue()
    
    print(pq)    
    print(pq.is_empty())
    
    pq.put("last", 5)
    pq.put("third", 4)
    pq.put("first", 1)
    pq.put("second", 2)
    
    print(pq)
    
    print(pq.get())
    print(pq)
    
    print(pq.get())
    print(pq)
    
    

        
    
    
