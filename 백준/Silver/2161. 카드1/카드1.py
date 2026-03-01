n=int(input())
queue=[]
for i in range(n):
    queue.append(i+1)
for j in range(n):
    print(queue.pop(0))
    if queue:
        queue.append(queue.pop(0))