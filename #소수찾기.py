#소수찾기

a=int(input())
finding_number=list(map(int,input().split(" ")))

cnt = 0

for i in range(a):
    pn = True
    for j in range(2, finding_number[i]):
        if (finding_number[i]%j)==0 :
            pn= False
            break
    if(pn==True) and(finding_number[i]!=1):
        cnt+=1

print(cnt)

