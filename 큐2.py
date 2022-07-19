import sys

input= sys.stdin.readline

n = int(input())

s = []

for i in range(n):
    st = input().split()
    if st[0] == 'push':
        s.append(st[1])
    elif st[0]=='pop':
        if not s:
            print("-1")
        else: 
            print(s.pop(0))
    elif st[0] == 'size':
        print(len[s])
    elif st[0] =='empty':
        if not s :
            print('1')
        else: 
            print('0')
    elif st[0]=='front':
        if not s:
            print(-1)
        else: 
            print(s[0])
    elif st[0]=='back':
        if not s:
            print(-1)
        else: 
            print(s[-1])
# 런타임 에러...왜?? 