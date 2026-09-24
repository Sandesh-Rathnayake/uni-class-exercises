stack=[]
max_size=6

if len(stack)<max_size:
    stack.append(5)
    print("stack is:",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.append(15)
    print("stack is:",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.append(25)
    print("stack is:",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.pop(0)
    print("stack is after the DEQUEUE :",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.append(35)
    print("stack is:",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.append(45)
    print("stack is:",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.pop(0)
    print("stack is after the DEQUEUE :",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.append(55)
    print("stack is:",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    print("stack's peek value is :",stack[0])
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.append(65)
    print("stack is:",stack)
else:
    print("Stack Underflow")