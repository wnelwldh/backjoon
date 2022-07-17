a =[]
def push(i):
    a.append(i)
def pop():
    if len(a) == 0:
        print(-1)
    else: 
     print(a[-1])
     a.pop()

def size(a):
    print(len(a))

def empty(a):
    if len(a) == 0:
        print(1)
    else:
        print(0)
def top(a):
    if len(a)>0:
        print(a[-1])
    else: 
        print(-1)

n = int(input())
k = [input()for _ in range(n)]

for i in range(n):
    if "push" in k[i]:
        push(k[1].split()[1])
    elif k[1]=="top":
        top(a)
    elif k[1] == "size":
        size(a)
    elif k[1] == "empty":
        empty(a)
    elif k[1] =="pop":
        pop()
        