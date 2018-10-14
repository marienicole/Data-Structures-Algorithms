
# basic Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, root, node):
        if root is None:
            self.root = node
        else:
            if root.val < node.val:
                if root.right == None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left == None:
                    root.left = node
                else:
                    self.insert(root.left, node)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)


    def search(node, key):
        if node is None or node.val == key:
            return node
        elif root.val < key:
            return self.search(root.right, key)
        else: # root.val is greater than key
            return self.search(root.left, key)

def main():
    root_val = input("Please provide a value for root node > ")
    n = Node(root_val)
    t = Tree(n)
    choice = 0
    while choice != 3:
        print("Usage:\n\t1: New Node\n\t2: Print\n\t3: Quit\n")
        choice = int(input("Provide your choice > "))
        if choice == 1:
            val = input("Please enter node value > ")
            t.insert(t.root, Node(val))
        elif choice == 2:
            t.inorder(t.root)
        else:
            print("Goodbye!")
            exit()

main()
