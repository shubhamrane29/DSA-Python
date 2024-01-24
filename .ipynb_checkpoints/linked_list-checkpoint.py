class Node:
    #Create a node
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        #Reference of the 1st node
        self.head = None

    def print_LL(self):
        if self.head is None:
            print('Linked List is empty!')
        
        else:
            n = self.head
            while n is not None:
                print(f'{n.data} ->', end = ' ')
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        #Making the ref of 2nd node in 1st node head
        new_node.ref = self.head
        #This is the reference of 1st node
        #Getting replaced by new node
        self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)

        #when the list is empty
        if self.head is None:
            self.head = new_node

        else:
            n = self.head
            #Finding where ref is none i.e., last node
            while n.ref is not None:
                n = n.ref
            n.ref = new_node


if __name__ == '__main__':
    ll = Linkedlist()
    ll.add_begin(29)
    ll.add_end(17)
    ll.add_begin(36)
    ll.add_end(9)
    ll.print_LL()