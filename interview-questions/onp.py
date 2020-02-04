import sys
def to_postfix(infix_str):
    stack = []
    ops = ["+","-","*","/","^"]
    output = ""
    for c in infix_str:
        if c == '(':
            stack.append(c)
        elif c in ops:
            while(stack is not [] and stack[-1] in ops and ops.index(c) <= ops.index(stack[-1])):
                if stack.top() in ops:
                    if ops.index(c) <= ops.index(stack[-1]):
                        output = output + stack[-1]
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                output = output + stack[-1]
                stack.pop()
            stack.pop()
        else:
            output = output + c
    return output

if __name__ == '__main__':
    amount = int(input())
    equations = []
    for i in range(amount):
        equations.append(input().strip())
    for equation in equations:
        print(to_postfix(equation))
