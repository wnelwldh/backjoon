n = int(input())
def check(b):
    st =[]
    for i in b:
        if i == "(":
            st.append(i)
        else:
            if not st:
                print("NO")
                return
            else:
                st.pop()
    if not st:
        print("YES")
        return
    else: 
        print("NO")
        return
for _ in range(n):
    b = input()
    check(b)
    #  틀렸다가 맞음 -> 대문자 구별 안함