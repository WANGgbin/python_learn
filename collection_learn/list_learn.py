stack = [1, 2, []]
stack1 = stack[:]
print(id(stack), id(stack1))
stack1[2].append(1)
print(stack)
stack1[2] = 3
print(stack)