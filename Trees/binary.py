class Tree():
    def __init__(self, data, parent, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data

    def set_data(self, data):
        self.data = data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_parent(self):
        return self.parent

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def add_child(self, node_data):
        if (self.left == None):
            self.left = Tree(node_data, self)
            print "\n" + str(node_data) + " was added as left child of " + str(self.data)
            return self

        elif (self.right == None):
            self.right = Tree(node_data, self)
            print "\n" + str(node_data) + " was added as right child of " + str(self.data)
            return self.left



def usage():
    print "\n\t1: Add a new node"
    print "\t2: Exit\n"
    choice = input("Please Enter Your Choice: ")
    return choice

# TODO: currently only prints the most recent left node

def get_input():
    node_data = input("Please Enter a New Node: ")
    return int(node_data)


def main():
    global tree
    global root
    global current

    level = 0
    node_data = input("Please Enter a New Node: ")
    tree = Tree(node_data, None)
    root = tree
    current = tree

    choice = 1
    while (choice != 2):
        choice = int(usage())

        if (choice == 1): # add node
            data = get_input()
            current = current.add_child(data)


main()
