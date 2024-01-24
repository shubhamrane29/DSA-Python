def using_list():
    queue = []

    def enqueue():
        a = int(input('Enter number you want to add: '))
        queue.append(a)
        print(queue)

    def dequeue():
        if not queue:
            print('Queue is empty!')
        else:
            p = queue.pop(0)
            print(p, 'was popped')
            print(queue)

    while True:
        choice = int(input('Select 1. Add 2. Remove 3. Quit: '))
        if choice == 1:
            enqueue()
        elif choice == 2:
            dequeue()
        elif choice == 3:
            break
        else:
            print('Please choose a valid number')

def collections_module():
    def adding_from_left():
        import collections
        q = collections.deque()
        q.appendleft(10)
        q.appendleft(20)
        q.appendleft(30)
        print(q)
        q.pop()
        print(q)
    
    def adding_from_right():
        import collections
        q = collections.deque()
        q.append(10)
        q.append(20)
        q.append(30)
        print(q)
        q.popleft()
        print(q)

    
    choice = int(input('1. Append from Left 2. Append from Right: '))
    if choice == 1:
        adding_from_left()
    elif choice == 2:
        adding_from_right()
    else:
        print('Invalid Number')

def queue_method():
    import queue
    q = queue.Queue()
    #Operation is carried out in location
    q.put(10)
    q.put(50)
    q.put(20)
    print(q.get())

def priority():
    import queue
    q = queue.PriorityQueue()
    q.put(20)
    q.put(60)
    q.put(10)
    q.put(50)
    #Lowest Number Removed first
    print(q.get())
    print(q.get())

priority()

