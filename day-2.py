stack=[]
max_size=6

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
    stack.append(35)
    print("stack is:",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.pop()
    print("stack is:",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.append(45)
    print("stack is:",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.append(55)
    print("stack is:",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    print("stack's peek value is:",stack[-1])
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.pop()
    print("stack is:",stack)
else:
    print("Stack Underflow")

if len(stack)<max_size:
    stack.append(65)
    print("stack is:",stack)
else:
    print("Stack Underflow")