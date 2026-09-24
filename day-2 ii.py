stack1 = [12, 25, 38, 41, 56]
stack2 = [12, 25, 38, 41, 60]

while len(stack1)>0 and len(stack2)>0:
    stack1.pop()
    stack2.pop()
    print(f"Popped from stack1: {stack1}, Popped from stack2: {stack2}")

if len(stack1) == len(stack2):
    print("Stacks are equal")
else:
    print("Stacks are not equal")
    