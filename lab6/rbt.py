class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        temp = self.left
        temp.parent = self.parent
        if self.parent != None and self.is_left_child():
            self.parent.left = temp
        elif self.parent != None:
            self.parent.right = temp
        self.left = temp.right
        if temp.right != None:
            temp.right.parent = self
        temp.right = self
        self.parent = temp

    def rotate_left(self):
        temp = self.right
        temp.parent = self.parent
        if self.parent != None and self.is_left_child():
            self.parent.left = temp
        elif self.parent != None:
            self.parent.right = temp
        self.right = temp.left
        if temp.left != None:
            temp.left.parent = self
        temp.left = self
        self.parent = temp



class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        if node.parent == None:
            node.make_black()
        while node != None and node.parent != None and node.parent.is_red(): 
            # if uncle is red
            if not node.uncle_is_black():
                node.parent.colour = "B"
                node.get_uncle().colour = "B"
                node.parent.parent.colour = "R"
                self.fix(node.parent.parent)
            # if uncle is black
            else:
                # left left case
                if node.is_left_child() and node.parent.is_left_child():
                    node.parent.parent.colour = "R"
                    node.parent.colour = "B"
                    if self.root == node.parent.parent:
                        self.root = node.parent
                    node.parent.parent.rotate_right()
                    self.fix(node.parent)
                # left right case
                elif node.is_right_child() and node.parent.is_left_child():
                    node.parent.parent.colour = "R"
                    node.colour = "B"
                    if self.root == node.parent.parent:
                        self.root = node
                    node.parent.rotate_left()
                    node.parent.rotate_right()
                    self.fix(node)
                # right right case
                elif node.is_right_child() and node.parent.is_right_child():
                    node.parent.parent.colour = "R"
                    node.parent.colour = "B"
                    if self.root == node.parent.parent:
                        self.root = node.parent
                    node.parent.parent.rotate_left()
                    self.fix(node.parent)
                # right left case
                else:
                    node.parent.parent.colour = "R"
                    node.colour = "B"
                    if self.root == node.parent.parent:
                        self.root = node
                    node.parent.rotate_right()
                    node.parent.rotate_left()
                    self.fix(node)
        self.root.make_black()
                    
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"

# a = RBTree()
# a.insert(10)
# a.insert(5)
# a.insert(6)
# a.insert(9)
# #a.insert(15)
# a.insert(8)


# print(a)
# print(a.root)