#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Python program to construct tree using inorder and
 preorder traversals"""
 
# A binary tree node 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# search from the inOrder array
def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i

# print the tree
def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print (node.data)
    printInorder(node.right)

""" 1. Function to construct binary  tree """
def buildTree(inOrder, preOrder, inStrt, inEnd):
     
    if (inStrt > inEnd):
        return None
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if inStrt == inEnd :
        return tNode

    inIndex = search(inOrder, inStrt, inEnd, tNode.data)

    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1)
    tNode.right = buildTree(inOrder, preOrder, inIndex+1, inEnd)
    return tNode
 
""" 2. Function to print the Left Child given a node value"""  
def returnLeftElement(tree, item):
    if tree is None:
        return
    if tree.data == item:
        print ("The left child of "+tree.data+" is: "+tree.left.data)
    elif tree.left.data==item:
        returnLeftElement(tree.left, item)
    elif tree.right.data==item:
        returnLeftElement(tree.right, item)
    else:
        print ("Searched element "+item+" do not have a left child!")

""" 3. Function to print the Right Child given a node value"""
def returnRightElement(tree, item):
    if tree is None:
        return
    if tree.data == item:
        print ("The right child of "+tree.data+" is: "+tree.right.data)
    elif tree.left.data==item:
        returnRightElement(tree.left, item)
    elif tree.right.data==item:
        returnRightElement(tree.right, item)
    else:
        print ("Searched element "+item+" do not have a right child!")   


""" 4. Function to change the root node"""  
def changeRoot(tree, newData):
    if tree is None:
        return
    tree.data = newData
    print ("New root updated inorder traversal of the tree is")
    printInorder(tree)
     
    
    
    
    
# Input tree values in the form of InOrder list & PreOrder list
inOrder = ['D', 'B' ,'E', 'A', 'F', 'C', 'G']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F', 'G']

buildTree.preIndex = 0
myTree = buildTree(inOrder, preOrder, 0, len(inOrder)-1)
 
# print the constructed tree
print ("Inorder traversal of the constructed tree is")
printInorder(myTree)
print ("\n")

#output for sample inputs for left & right child returning functions
print ("Sample outputs for left & right child returning functions")
returnLeftElement(myTree, "A")
returnLeftElement(myTree, "B")
returnLeftElement(myTree, "C")
returnLeftElement(myTree, "G")
returnRightElement(myTree, "A")
returnRightElement(myTree, "B")
returnRightElement(myTree, "C")
returnRightElement(myTree, "F")
print ("\n")

# print the newly updated tree given an input change
changeRoot(myTree, "X")