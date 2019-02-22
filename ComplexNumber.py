class Complex:
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def __add__(self,other):
		return(Complex(str(self.a + other.a),str(self.b + other.b)))

	def __sub__(self,other):
		return (Complex(str(self.a - other.a), str(self.b - other.b)))

	def __mul__(self,other):
		n1,n2 = self.a * other.a, self.a * other.b
		n3,n4 = self.b * other.a, self.b * other.b
		return str(n1+(-n4)) + " + " + str(n2+n4)+"i"

	def __str__(self):
		return str(self.a) + " + " + str(self.b) + "i"
