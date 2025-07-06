from collections import deque
people = ["Alice","Bob","Charlie","David","Leo"]
wait_time = [4,2,5,6,3]
time = 1
queue =deque(people)
queue_time = deque(wait_time)
print(queue)
print(queue_time)

while len(queue) != 0:
    guy = queue.popleft()
    if queue_time.popleft() > time:
        print(f"{guy} got the ticket at the time",time)
    else:
        print(f"{guy} left out frustation at",time)
    time += 1