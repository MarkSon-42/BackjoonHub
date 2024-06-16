import sys
import heapq as hq

input = sys.stdin.readline

num_elements = int(input())

priority_queue = []

for _ in range(num_elements):
    element = int(input())
    
    if element:
        hq.heappush(priority_queue, (-element, element))
    else:
        if len(priority_queue) >= 1:
            print(hq.heappop(priority_queue)[1])
        else:
            print(0)