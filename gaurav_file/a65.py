#example in mro

# Python program showing
# how MRO works

class A:
	def rk(self):
		print(" In class A")
class B(A):
	def rk(self):
		print(" In class B")

r = B()
r.rk()

