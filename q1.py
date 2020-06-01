import math
a=[2,3,4,5,6,7]
j=1
for k in a:
    for i in range(10):
        x=((j+k/j)/2)
        j=x
    # print(math.sqrt(k))
    if math.sqrt(k)==j:
        print(f"a is {k} and fixed point of the iteration is ",end=" ")
        # print(u"\u221a",end="")
        print(f"square root of a which is {j}")
print()
def square_root(n):
    a=int(input("upto what accuracy is sufficient? "))
    i=int(input("Enter number of iterations u want? "))
    k=1
    for j in range(i):
        j=(k+n/k)/2
        k=j
    print(f"Result is {round(k,a)}")
i='y'
while i!='n' or i=='N':
    if i=='y' or i=='Y':
        n=float(input("Enter the number to get square root ? "))
        print()
        square_root(n)
        print()
        print("----------------------------------------------------------------")
        print()
    else:
        print("Try again")
    i=input("Want to continue ? press y (for yes) or n (for no) : ").strip()
    print()
    print("--------------------------------------------------------------------")
    print()
