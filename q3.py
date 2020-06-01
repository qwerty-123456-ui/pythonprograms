import time

print()
def fib_iter(n):
    a = 0
    b = 1
    # print("Fibonacci series ( using iterative method ) is : ")
    # print(a,b,end=" ")
    for i in range(n - 2):
        c = a + b
        a = b
        b = c
        # print(c,end=" ")
    return c

def fib_rec(n):
    a = 0
    b=1
    if n <= 0:
        print("No series")
    else:
        if n == 1:
            return a
        elif n == 2:
            # print("1")
            return b
        else:
            # print(fib_rec(n-2)+fib_rec(n-1),end=" ")
            return fib_rec(n - 2) + fib_rec(n - 1)


# print("Fibonacci series ( using recursive method ) is : ")
ci=0
cr=0
for i in range(10,31,5):
    print(f"{i}th Fibonacci number ( using iterative method ) is : ",end=" ")
    t1 = time.time()
    print(fib_iter(i))
    t2 = time.time()
    ti = t2 - t1
    print(f"time taken taken by iterative method : {t2 - t1}")
    print()
    print(f"{i}th Fibonacci number ( using recursive method ) is : ",end=" ")
    t3 = time.time()
    print(fib_rec(i))
    t4 = time.time()
    tr = t4 - t3
    print(f"time taken taken by iterative method : {t4 - t3}")
    print()
    if tr > ti:
        print("iterative method is faster")
        ci+=1
    else:
        print("recursive method is faster")
        cr+=1
    print()
    print("--------------------------------------------------------------------------------")
    print()
print(f"Number of times iterative method is faster is : {ci} and number of times recursive method is faster is : {cr}")
print()
