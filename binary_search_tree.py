#Binary Search Tree
class BST:
    def __init__(self, key):
        #Key, right child, left child
        self.key = key
        self.lchild = None
        self.rchild = None

        print(self.key, end=' ')

    def insert(self, data):
        #if tree is empty
        if self.key is None:
            self.key = data
            return
        
        #Duplicate value
        if self.key == data:
            return

        #Travelling to left subtree
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)

        #Travelling to right subtree
        elif self.key < data:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        #if data is found
        if self.key == data:
            print(f'{data} is present')
            return
        
        #if data value is smaller than the key value
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('Node not present')
        
        #if data value is greater than the key value
        elif self.key < data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('Node not found')

    def delete(self, data, curr):
        #Empty tree
        if self.key is None:
            print('The tree is empty')
            return
        
        #Travelling the left side of root node
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print('Node not present')

        #Travelling the right side of root node
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print('Node not present')

        #Deleting the data
        else:
            #Deleting if no or right node is present
            if self.lchild is None:
                return self.rchild

            if self.rchild is None:
                return self.lchild

            #Node with two child node
            #Replace with smallest value of right sub tree

            node = self.rchild
            while node.lchild:
                node = node.lchild

            self.key = node.key
            #Deleting the value after replacing
            self.rchild = self.rchild.delete(node.key, curr)
    
        return self

    def preorder(self):
        #printing the root node
        print(self.key, end=" ")

        #printing the left node
        if self.lchild:
            self.lchild.preorder()
        
        #printing the right node
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        #printing the left node
        if self.lchild:
            self.lchild.inorder()

        #print the root
        print(self.key, end=" ")

        #print the right node
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        #printing left node
        if self.lchild:
            self.lchild.postorder()

        #printing right node
        if self.rchild:
            self.rchild.postorder()
        
        #print the root
        print(self.key, end=" ")

    def min_node(self):
        if self.lchild:
            self.lchild.min_node()
        else:
            print('Minimum Node:', self.key)

    def max_node(self):
        if self.rchild:
            self.rchild.max_node()
        else:
            print('Maximum Node:', self.key)


if __name__ == '__main__':
    root = BST(20)

    insert_list= [10,30,8,12,25,35,40,11,9,7]
    for i in insert_list:
        root.insert(i)

    print()
    print('Preorder')
    root.preorder()
    print()
    print('Postorder')
    root.postorder()
    print()
    print('Inorder')
    root.inorder()

    if root.lchild is None and root.rchild is None:
        print("Can't perform delete operation")
    else:
        root.delete(20, root.key)

    print()
    print('Inorder after deletion:')
    root.inorder()

    print()
    root.min_node()
    root.max_node()