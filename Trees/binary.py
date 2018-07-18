class Node():
    def __init__(self, data, level, parent=None, left=None, right=None):
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
        
    def get_leve(self):
        return self.level

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right
    # def add_child(self, node_data):
    #     if (self.left == None):
    #         self.left = Tree(node_data, self)
    #
    #     elif (self.right == None):
    #         self.right = Tree(node_data, self)


class Tree():
    def __init__(self, root=None):
        self.root = root
        nodes = {}
        if self.root:
            nodes.append(root, root.get_data())
        # dictionary of nodes
        # insert each new node in respective place
        # shift others accordingly


    def get_root(self):
        return self.root

    def add_node(self, data, parent):

        if parent.right_node(): # if parent already has two nodes
            print "Error: Node already has two children\n"

        elif not parent.left_child(): # if no left node has been set
            new = Node(data, parent)
            parent.set_left(node)
            print str(new.data) + " is the left child of " + str(parent.data)

        elif not parent.right_child(): # if parent has no right node
            new = Node(data, parent)
            parent.set_right(node)
            print str(new.data) + " is the right child of " + str(parent.data)

        else:
            print "Unknown error, sorry bout it i guess\n"



def main():


main()
