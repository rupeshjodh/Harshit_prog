# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)


#generator in fibonacci


def fibonacci(n):
	a=0
	b=1
	if n==1:
		print(a)
	else:
		if n==2:
			print(a,b)
		else:
			print(a,b,end=" ")
			c=a+b
			a=b
			b=c
			(yield c )

fibonacci(5)
