import sys

""" 
Given the root node of a binary search tree (BST) and a value. 
You need to find the node in the BST that the node's value equals the given value. 
Return the subtree rooted with that node. 
If such node doesn't exist, you should return NULL.
"""

# Definition for a binary tree node. (Given)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Insert value into Binary Search Tree
def insert(root, node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
  
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 

def searchBinaryTree(root, val):
    if root == None:
        print("Value does not exist in current tree.")
    elif val == root.val:
        inorder(root)
    elif val > root.val:
        root = root.right
        searchBinaryTree(root, val)
    else:
        root = root.left
        searchBinaryTree(root, val)

# Main Program 
if __name__ == "__main__":
    val = 90
    r = TreeNode(50) 
    insert(r, TreeNode(30)) 
    insert(r, TreeNode(60)) 
    insert(r, TreeNode(20)) 
    insert(r, TreeNode(40)) 
    insert(r, TreeNode(70)) 
    insert(r, TreeNode(80)) 
    searchBinaryTree(r, val)