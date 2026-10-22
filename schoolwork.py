stack = [0,0,0,0,0]
top = 0

def push(item):
    global top,stack
    if top == 5:
        print("Stack is full!")
    else:
        stack[top] = item
        top = top+1

def pop():
    global top,stack
    if top == 0:
        print("Stack is empty!")
    else:
        top = top-1
        item = stack[top]   
        return item
print(pop())
push(2)
push(8)
push(-4)
push(16)
push(42)
push(64)
print(stack)
print(pop())