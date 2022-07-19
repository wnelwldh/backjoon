n = int(input())
def check(b):
    st =[]
    for i in b:
        if i == "(":
            st.append(i)
        else:
            if not st:
                print("no")
                return
            else:
                st.pop()
    if not st:
        print("yes")
        return
    else: 
        print("no")
        return
for _ in range(n):
    b = input()
    check(b)