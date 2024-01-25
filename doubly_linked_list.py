class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None #Next node reference
        self.pref = None #previous node reference

class Double_Linked:
    def __init__(self):
        self.head = None

    def print_dll(self):
        if self.head is None:
            print('Linked List is empty!')
        else:
            n = self.head
            while n is not None:
                print(f'{n.data} ->', end = ' ')
                n = n.nref
            print('None')
    
    def print_dll_reverse(self):
        if self.head is None:
            print('Linked List is empty!')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref

            while n is not None:
                print(f'{n.data} ->', end = ' ')
                n = n.pref
            print('None')

    def at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    def at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref           
            n.nref = new_node
            new_node.pref = n
    
    def add_after(self, data, x):
        if self.head is None:
            print('Linked List is empty!')
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref

            if n is None:
                print('Node not present in the list')
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                n.nref.pref = new_node
                n.nref = new_node
                new_node.pref = n
                

    def add_before(self, data, x):
        if self.head is None:
            print('Linked List is empty!')
        else:
            n = self.head
            while n.nref is not None:
                if n.nref.data == x:
                    break
                n = n.nref
            
            if n.nref is None:
                print('Node is not present in Linked List')
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                n.nref.pref = new_node
                n.nref = new_node

    def delete_begin(self):
        if self.head is None:
            print('Linked List is empty!')
        elif self.head.nref is None:
            self.head = None
            print('Now linked list is empty after deletion!')
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print('Linked List is empty!')
        elif self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref.nref is not None:
                n = n.nref
            n.nref.pref = None
            n.nref = None

    def delete_byvalue(self, x):
        if self.head is None:
            print('Linked List is empty')
        elif self.head.data == x:
            self.head = self.head.nref
        else:
            n = self.head
            while n.nref is not None:
                if n.data == x:
                    break
                n = n.nref
        
        if n.nref is None:
            print('Node is not present in Linked List')
        else:
            n.pref.nref = n.nref
            n.nref.pref = n.pref

if __name__ == '__main__':
    dll = Double_Linked()
    dll.at_end(25)
    dll.at_begin(32)
    dll.at_end(43)
    dll.add_after(11, 32)
    dll.add_before(16, 43)
    dll.print_dll() #32->11->25->16->43->None
    dll.delete_begin()
    dll.delete_end()
    dll.delete_byvalue(25)
    dll.print_dll() #11->16->None
    dll.print_dll_reverse() #16->11->None
    