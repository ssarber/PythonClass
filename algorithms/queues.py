# first element added is the first element retrieved (“first-in, first-out”)

from collections import deque

queue = deque(["Arombo", "Jones", "Pukk"])
queue.append("terry")
queue.popleft()

print(queue)