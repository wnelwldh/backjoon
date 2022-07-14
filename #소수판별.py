#소수판별
def number(a):
    if a<2: 
        return False
    else:
        for i in range(2, int(a**0.5+1)):
            if a%i == 0:
                return False
            
        return True

b=[1,2,3,4,5,6,7]
for i in b:
    print(number(i))
