class Tree():
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def set_data(self, data):
        self.data = data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_data(self):
        return self.data

    def add_child(self, node_data):
        if (self.left == None):
            print "\n\tadding left node"
            self.left = Tree(node_data)
            return self

        elif (self.right == None):
            print "\n\tadding right node"
            self.right = Tree(node_data)
            return self.left




def usage():
    print "\n\t1: Add a new node"
    print "\t2: Print the Tree"
    print "\t3: Exit\n"
    choice = input("Please Enter Your Choice: ")
    return choice

# TODO: currently only prints the most recent left node

def print_tree(node):
    if (node.left == None and node.right == None): # no left or right node, we just return data
        print(str(node.get_data()) + "\n")

    elif (node.left != None): # left node exists, recurse with left
        return print_tree(node.left)

    elif (node.right != None): # we've already been through the left nodes
        return print_tree(node.right)


def get_input():
    node_data = input("Please Enter a New Node: ")
    return int(node_data)


def main():
    global tree
    global root
    global current

    node_data = input("Please Enter a New Node: ")
    tree = Tree(node_data)
    root = tree
    current = root

    choice = 1
    while (choice != 3):
        choice = int(usage())

        if (choice == 1):
            data = get_input()
            current = current.add_child(data)

        elif (choice == 2):
            print_tree(tree)

main()
