#!/usr/bin/env python
# code heavily based on:
# http://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python-are-there-any-built-in-data-structures-in

import hashlib

def sha256(data):
	m = hashlib.sha256()
	m.update(data)
	return int(m.digest().encode('hex'),16)
	
class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
	self.hash = sha256(self.data)
    def __repr__(self,):
	return "node: %x64s, data: [%s]" % (self.hash,self.data)

class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node , data):
	hash = sha256(data)
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        if node is None:
	    #print "empty"
            return self.createNode(data)
        # if hash is smaller than parent , insert it into left side
        if hash < node.hash:
            node.left = self.insert(node.left, data)
	    #print "left"
        elif hash > node.hash:
            node.right = self.insert(node.right, data)  
	    #print "right"
		
        return node


    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        # if root is None or root is the search data.

	return self.search_by_hash(node,sha256(data))

    def searchByHash(self,node,hash):
	if node is None or node.hash == hash:
	    return node
        if node.hash < hash:
            return self.searchByHash(node.right, hash)
        else:
            return self.searchByHash(node.left, hash)

	
    def deleteNode(self,node,data):
	hash = sha256(data)
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarion that we can handle
        Now it is handling only leaf.
        """
	return self.deleteNodeByHash(node,sha256(data))

    def deleteNodeByHash(self,node,hash):
        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if hash < node.hash:
            node.left = self.deleteNodeByHash(node.left, hash)
        elif hash > node.hash:
            node.right = self.deleteNodeByHash(node.right, hash)
        else: # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return  temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

        return node

    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverseInorder(root.left)
	    print root
            self.traverseInorder(root.right)

    def traversePreorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print root
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)
	    print root

