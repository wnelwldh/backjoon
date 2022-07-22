import collections as cl

a= int(input())
n = cl.deque([i for i in range(1,a+1)])

while len(n)>1:
    n.popleft()
    n.rotate(-1)
    
print(n[0])