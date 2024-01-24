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

    def add_after(self, data, x):
        n = self.head
        #When node is present
        while n is not None:
            if n.data == x:
                break
            # Moving n to next data
            n = n.ref
        if n is None:
            #When node is not present
            print('Node is not present in Linked List')

        else:
            #When node is present and we found x
            new_node = Node(data)
            #x ref i.e., the next node is now new node ref 
            new_node.ref = n.ref
            #new node ref is given to the previous node i.e., x
            n.ref = new_node

    def add_before(self, data, x):
        n = self.head
        #If list is empty
        if n is None:
            print('Linked List is empty!')
            return
        
        #Adding element at beginning
        if n.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        
        #Looping through the list
        while n.ref is not None:
            #Check next node data, while being on previous node
            if n.ref.data == x:
                break
            n = n.ref

        #Number not found after looping the list
        if n.ref is None:
            print('Node not present in Linked List')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_empty(self, data):
        if self.head is not None:
            print('Linked List is not empty!')
        else:
            new_node = Node(data)
            self.head = new_node

    def delete_begin(self):
        if self.head is None:
            print('Linked List is empty!')
        else:
            self.head = self.head.ref

    def delete_end(self):
        n = self.head
        if n is None:
            print('Linked List is empty!')
        else:
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_node(self, data):
        #Check if list is empty
        if self.head is None:
            print('Linked List is empty!')
            return
        
        #If first node is to be deleted 
        if self.head.data == data:
            self.head = self.head.ref
            return
        
        n = self.head
        while n.ref is not None:
            if n.ref.data == data:
                break
            n = n.ref

        #Node not found
        if n.ref is None:
            print('Node not present in Linked List')
        else:
            n.ref = n.ref.ref


if __name__ == '__main__':
    ll = Linkedlist()
    ll.add_empty(1)
    ll.add_begin(29)
    ll.add_end(9)
    ll.add_begin(36)
    ll.add_after(56, 1)
    ll.add_before(43,9)
    #36->29->1->56->43->9
    ll.delete_begin() #Delete 36
    ll.delete_end() #Delete 9
    ll.delete_node(56) #Delete 56
    ll.print_LL()
    #29->1->43