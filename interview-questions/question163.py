from queue import LifoQueue as Stack
def fun(lst):
    stack = Stack()
    for value in lst:
        if(isinstance(value,str)):
            operand1 = stack.get()
            operand2 = stack.get()
            if(value == "+"):
                stack.put(operand2+operand1)
            if(value == "-"):
                stack.put(operand2-operand1) 
            if(value =="*"):
                stack.put(operand2*operand1)
            if(value == "/"):
                stack.put(operand2//operand1)
        else:
            stack.put(value)
    return stack.get()
if __name__ == "__main__":
    print(fun([5,3,'+']))
    print(fun([15,7,1,1,'+','-','/',3,'*',2,1,1,'+','+','-']))
