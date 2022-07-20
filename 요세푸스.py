from unittest import result


N,K= map(int,input().split())

cl = [i for i in range(1, N+1)]
r = []
p = 0

for _ in range(N):
    p += K-1
    if p >= len(cl):
        p %= len(cl)
    r.append(cl.pop(p))
    
print("<",", ".join(map(str,r)),">",sep="")