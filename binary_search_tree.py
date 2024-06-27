# Binary Search Tree
# Nodes - each node is BST itself
# 3 attributes - .value, .left, .right



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<BST|{self.value}>"

    # Method to insert a new node into the tree
    def insert(self, new_value):
        # If the new value is less than the current node's value
        if new_value < self.value:
            # Look at the current node's left tree and see if its empty
            if self.left is None:
                # Set the left subtree to be the new instance of BST with the new value
                self.left = BST(new_value)
            # If the left subtree is not empty
            else:
                # Recursively call the insert method from the left subtree
                self.left.insert(new_value)
        # If the new value is greater than or equal to the current node's value
        else:
            # Look at the current node's right tree and see if its empty
            if self.right is None:
                # Set the right subtree to be the new instance of BST with the new value
                self.right = BST(new_value)
            # If the right subtree is not empty
            else:
                # Recursively call the insert method from the right subtree
                self.right.insert(new_value)

    # Method to find a node base on a value - will either return the BST Node instance or None
    def find_node(self, target):
        # If the target is equal to the current node's value
        if target == self.value:
            # We found the node, return it!
            return self
        # If the target is less than the current node's value
        elif target < self.value:
            # See if the left subtree is empty
            if self.left is None:
                # We know the target is not in the tree because it would be here (or at least on this path)
                return None
            # if the current node does have a left subtree
            else:
                # Call the find_node method from the left subtree and return that value
                return self.left.find_node(target)
        # If the target is greater than the current node's value
        elif target > self.value:
            # See if the right subtree is empty
            if self.right is None:
                # We know the target is not in the tree because it would be here (or at least on this path)
                return None
            # if the current node does have a right subtree
            else:
                # Call the find_node method from the right subtree and return that value
                return self.right.find_node(target)

    # Method to find the max value in a tree
    def find_max(self):
        # If the right is empty
        if self.right is None:
            # The this is the largest value
            return self
        # If it is not empty
        else:
            # Move to the right, and call find max on that node
            return self.right.find_max()

    # Method to find the min value in a tree
    def find_min(self):
        # If the left is empty
        if self.left is None:
            # The this is the largest value
            return self
        # If it is not empty
        else:
            # Move to the left, and call find min on that node
            return self.left.find_min()

    # Method to remove a node from the tree
    def delete(self, target, parent=None):
        # Find the Node to remove
        if target < self.value:
            # If the target is less than the current node's value, move to the left and try again
            if self.left:
                self.left.delete(target, self) # Recursively search through the left subtree
        elif target > self.value:
            # If the target is greater than the current node's value, move to the right and try again
            if self.right:
                self.right.delete(target, self) # Recursively search through the right subtree
        # We have found the node (if not less than or greater than it must be equal to)
        else:
            # Case 1: Node we are trying to delete has two children
            if self.left and self.right:
                # Replace node's value with the maximum value from the left subtree
                self.value = self.left.find_max().value
                # Remove the node with the max value in the left subtree
                self.left.delete(self.value, self)
            # Case 2: Node is the root and has one or no children
            elif parent is None:
                # If the node only has a left subtree
                if self.left:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                # If the node only has a right subtree
                elif self.right:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                # Case 3: Root Node is a leaf
                else:
                    # Delete the tree
                    del self
            # Case 4: Node has one or no children and is the left child of its parent
            elif parent.left == self:
                # Update the parent's left pointer to point to the node's child
                parent.left = self.left if self.left else self.right
            # Case 5: Node has one or no children and is the right child of its parent
            elif parent.right == self:
                # Update the parent's right pointer to point to the node's child
                parent.right = self.left if self.left else self.right

    # Method to perform an in-order traversal
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def reverse_traversal(self):
        if self.right:
            self.right.reverse_traversal()
        print(self.value)
        if self.left:
            self.left.reverse_traversal()

my_tree = BST(50)
my_tree.insert(45)
my_tree.insert(22)
my_tree.insert(27)
my_tree.insert(87)
my_tree.insert(71)
my_tree.insert(93)
my_tree.insert(63)

print(my_tree.find_node(63))

my_tree.reverse_traversal()
