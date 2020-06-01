def power(x, y, p):
	res = 1
	x = x % p
	n=0
	while (y > 0):
		n+=1
		if (y & 1):
			res = (res * x) % p
			y=y-1
		else:
			y = y >> 1
			x = (x * x) % p

	return (res,n)

a=int(input("Enter the value of a in (a^n%m) : "))
n=int(input("Enter the value of n in (a^n%m) : "))
# remainderB = 0
m=int(input("Enter the value of m in (a^n%m) : "))
# for i in range(len(b)):
# 	remainderB = ((remainderB * 10 +int(b[i])) % (m - 1))
r,n=power(a, n, m)
print()
print (f"RESULT IS : {r} and NUMBER OF STEPS TAKEN : {n}")
print()
