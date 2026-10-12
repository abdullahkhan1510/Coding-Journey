stack = [None] * 5
top = -1


def push(item):
    global top
    if top == 4:
        print("Stack is full")
    else:
        top = top+1
        stack[top] = item

def peek():
    if top == -1:
        print("Stack is empty")
    else:
        return stack[top]

def pop():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        item = stack[top]
        stack[top] = None
        top = top-1
        return item
push(5)
push(10)
push(15)
push(20)
push(25)
print(pop())
print(pop())
print(peek())