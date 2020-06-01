from math import  log2,log,sin,cos,log10,sqrt,exp,pow,asin,acos,pi,ceil,floor,atan2,tan,atan,factorial
def f(n):
    # print(n)
    global fn
    n="("+str(n)+")"
    # print(n)
    # print(fn)
    fn=fn.replace('x',n)
    # print(fn)
    r=eval(fn)
    # print(r)
    fn=fn.replace(n,'x')
    # r=1
    return r

def integrate(a,b):
    h=(b-a)/2
    m=(a+b)/2
    r=h*(f(a)+4*f(m)+f(b))/3
    return r

def integrate_n(a,b,n):
    h=(b-a)/n
    # print(h)
    i=a
    r=0
    k=0
    while i<=b:
        if i==a or i==b:
            k+=1
            r+=f(i)
            # print(r)
        elif k%2!=0:
            k+=1
            r+=4*f(i)
            # print(r)
        else:
            k+=1
            r+=2*f(i)
            # print(r)
        i+=h
        # print(i)
    r=(r*h)/3
    return r

a=float(input("Enter a : "))
b=float(input("Enter b : "))
fn=input("Enter the function : ")
ch=input("if u want to enter value of subintervals ('n') then enter y (for yes) or n ( for no) : ")
if ch=='y' or ch=='Y':
    n=float(input("Enter the number of subinterval : "))
    print("Final result : ",integrate_n(a,b,n))
else:
    print("Final result : ",integrate(a,b))
