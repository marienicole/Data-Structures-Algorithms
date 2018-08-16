class Node():
    def __init__(self, data, level=0, parent=None, left=None, right=None):
        self.data = data
        self.level = level
        self.parent = parent
        self.left = left
        self.right = right

    def left_child(self):
        return self.left

    def right_child(self):
        return self.right

    def get_parent(self):
        return self.parent

    def get_data(self):
        return self.data

    def get_level(self):
        return self.level

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


class Tree():
    def __init__(self, root=None):
        self.current_level = 0
        self.root = root
        if self.root:
            self.current_level = 1

    def get_root(self):
        return self.root

    def add_node(self, data, parent):

        if parent.right_node(): # if parent already has two nodes
            print "Error: Node already has two children\n"

        elif not parent.left_child(): # if no left node has been set
            new = Node(data, parent)
            parent.set_left(node)
            print str(new.data) + " is the left child of " + str(parent.data)
            return new

        elif not parent.right_child(): # if parent has no right node
            new = Node(data, parent)
            parent.set_right(node)
            print str(new.data) + " is the right child of " + str(parent.data)
            return new

        else:
            print "Unknown error, sorry bout it i guess\n"



def main():

    input = input("Please enter a root node > ")
    tree = Tree(Node(input, 0))
    current = tree.get_root()

    while(choice != 1):
        print("Please choose from the list >")
        print("\t0: Enter a new Node\n\t1: Exit")
        if choice != 1:
            input = get_input()
            choice = int(input("Please enter a node value >"))
            current = tree.add_node(choice, current)

main()
