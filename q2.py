def Collatz_length(n):
    k,r,c=0,0,0
    while r!=1:
        if n%2==0:
            r=n/2
            c+=1
        else:
            r=3*n+1
            c+=1
        n=r

    # print(c)
    return c
m=0
l=[]
for i in range(2,21):
    print(f"Collatz length for {i} is :",end=" ")
    print(f"{Collatz_length(i)} ")
    if Collatz_length(i)>m:
        m=Collatz_length(i)
for i in range(2,21):
    if m==Collatz_length(i):
        l.append(i)
print(l)
print()
print(f"The longest Collatz length is {m} with n as {l}")
print()
