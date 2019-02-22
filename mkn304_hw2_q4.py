def e_approx(n):
	'''
	int -> int
	This Function takes a integer returns the approximation of euler's number.
	'''
	sum,fac = 1,1
	for i in range(1,n+1):
		fac *= i
		sum += 1/fac
	return sum

def main():
	for n in range(15):
		curr_approx = e_approx(n)
		approx_str = "{:.15f}".format(curr_approx)
		print("n =", n, "Approximation:", approx_str)
