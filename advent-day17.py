from collections import deque

step = 3
spinlock = deque([0])

for i in range(1,10):
    spinlock.rotate(-step)
    spinlock.append(i)
    print(spinlock)

print(spinlock[spinlock.index(0) + 1])