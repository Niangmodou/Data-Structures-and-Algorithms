class ArrayStack:
    def __init__(self):
        self.data=[];

    def __repr__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data);

    def is_empty(self):
        return len(self)==0;

    def push(self, item):
        self.data.append(item);

    def top(self):
        if self.is_empty():
           raise Exception("Stack is empty");
        return self.data[-1];

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty");
        return self.data.pop();

def eval_postfix_exp(exp): #exp is a list of the tokens
    operators='+-*/';
    args_stack = ArrayStack();
    for token in exp:
        if token not in operators:
            args_stack.push(int(token));
        else:
            rhs=args_stack.pop(); #right-hand-side
            lhs=args_stack.pop();
            if(token=='+'):
                res = lhs+rhs;
            elif(token=='-'):
                res = lhs-rhs;
            elif(token=='*'):
                res = lhs*rhs;
            else: #token=='/'
                res = lhs/rhs;
            args_stack.push(res);
    return args_stack.pop();


def print_in_reverse(st):
    s = ArrayStack();
    for ch in st:
        s.push(ch);

    while not s.is_empty():
        print(s.pop(), end='');
        

def main():
    pass
    #print_in_reverse('The Quick brown fox...');
    #print("The result is:", eval_postfix_exp(['2','3','4','*','+','5','-']));

#main();
