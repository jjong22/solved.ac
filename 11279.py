import heapq
import sys

input = sys.stdin.readline
print = sys.stdout.write

heap = []

n = input()

for i in range(int(n)):
    operation = int(input())
    if operation == 0:
        if heap:
            print(str(heapq.heappop(heap)[1]) + '\n')
        else:
            print(str(0) + '\n')
    else:
        heapq.heappush(heap, (-operation, operation))