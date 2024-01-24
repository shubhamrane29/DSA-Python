def using_list():
    stack  =[]
    def push():
        element = int(input('Enter a number to push: '))
        stack.append(element)
        print(stack)

    def pop():
        if not stack:
            print('Stack is empty!')
        else:
            p = stack.pop()
            print('The poped item is: ', p)
            print(stack)

    while True:
        choice = int(input('Select 1 for Push, 2 for Pop and 3 for quit: '))
        if choice == 1:
            push()
        elif choice == 2:
            pop()
        elif choice == 3:
            break
        else:
            print('Please enter the apropriate choice')

#using_list()
            
## Method 2
def using_modules():
    import collections

    def deque_method():
    #Deque: Double ended queue
        stack = collections.deque()
        stack.append(10)
        stack.append(20)
        stack.append(30)
        print(stack)

        stack.pop()
        print(stack)
    
    def queue_method():
        import queue
        stack = queue.LifoQueue(3)
        stack.put(10)
        stack.put(20)
        stack.put(30)
        print(stack)
        stack.get(timeout=1) #it won't print if last element is poped
        print(stack)