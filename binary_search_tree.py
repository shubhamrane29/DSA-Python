class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        #Tree is empty
        if self.key is None:
            self.key = data
            return
        
        #Duplicate value
        if self.key == data:
            return
        
        #Inserting to the left
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        
        #Inserting to the right
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key == data:
            print('Node is present')
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('Node not present')
        elif self.key < data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('Node not present')

    def preorder(self):
        print(self.key, end=' ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=' ')
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=' ')

    def delete(self, data):
        if self.key is None:
            print('The tree is empty')
            return

        if data < self.key:
            if self.lchild:
                #the left child of the current node (self.lchild) should be updated to the result of the delete operation on that left child
                self.lchild = self.lchild.delete(data)
            else:
                print('Node is not present')

        elif data > self.key:
            if self.rchild:
                #the right child of the current node (self.rchild) should be updated to the result of the delete operation on that right child
                self.rchild = self.rchild.delete(data)
            else:
                print('Node is not present')
        
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            
            #When deleting the node containing two child, we should replace it with either largest node in the left subtree or smallest node in the right subtree
            #We are replacing it with smallest node in the right subtree
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self


if __name__ == '__main__':
    root = BST(10)
    list1 = [6,3,1,6,98,3,7]
    for i in list1:
        root.insert(i)
    print('Preorder')
    root.preorder() #10,6,3,1,7,98
    print()
    root.delete(6)
    print('After Deleting')
    root.preorder() #10,7,3,1,98
    