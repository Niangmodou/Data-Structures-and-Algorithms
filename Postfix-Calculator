#Question 1

from ArrayStack import ArrayStack

def postixcalculator(expression,mydict):
	operators,temp = "-/+*",""
	user_input = expression.split(" ")
	stack = ArrayStack()

	for elem in user_input:
		if elem in operators:
			right = stack.pop()
			left = stack.pop()
			if elem == "+":
				stack.push(left + right)
			elif elem == "-":
				stack.push(left - right)
			elif elem == "*":
				stack.push(left * right)
			else:  # elem == "/"
				if right == 0:
					raise Exception("Divide by Zero Error")
				stack.push(left / right)
		elif elem in mydict:
			stack.push(mydict[elem])
		elif elem.isdigit():
			stack.push(int(elem))
		elif elem.isalpha():
			stack.push(elem)
			temp += elem

	if temp == "":
		val = stack.top()
		print(val)
	else:
		mydict[temp] = stack.top()
		print(temp)
		return(stack.top())

def main():
	dict = {}
	while True:
		user_input = input("--> ")
		if user_input == "done()":
			return
		postixcalculator(user_input,dict)
