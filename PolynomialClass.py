class Polynomial:
	def __init__(self,data=[0]):
		self.data = data

	def __add__(self,other):
		small = self
		big = other
		if len(self)>len(other):
			big = self
			small = other
		res = []
		for i in range(len(small)-1,-1,-1):
			res.append(big[i]+small[i])
		rem = big[-(len(big)-len(small)):]
		for i in rem:
			res.insert(0,i)
		return Polynomial(res[::-1])

	def __call__(self,num):

		return sum([(num**i)*self.data[i] for i in range(len(self.data))])

	def __len__(self):
		return len(self.data)

	def __getitem__(self,i):
		return self.data[i]

	def __str__(self):
		res = ""
		for i in range(len(self.data)-1,-1,-1):
			if self.data[i] != 0:
				res += str(self.data[i])
				res += "x^" + str(i) + " + "
		return res[:-2]

	def derive(self):
		for i in range(len(self.data)-1,-1,-1):
			self.data[i] *= i
		return self.data[1:]
