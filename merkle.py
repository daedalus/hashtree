#!/usr/bin/env python
# author Dario Clavijo 2016
# GPLv3

import hashlib

def sha256(data):
	m = hashlib.sha256()
	m.update(data)
	return int(m.hexdigest(),16)
	
class Node:
    """
    Class Node
    """
    def __init__(self, value,isRoot=False):
        self.left = None
        self.data = value
        self.right = None
	self.hash = sha256(self.data)
	self.isRoot = isRoot
    def __repr__(self,):
	return "__repr__ node: %64x, isRoot: %s, data: [%s]" % (self.hash,self.isRoot,self.data)

class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def __init__(self,):
	self.rootHash = None	
	self.leafcount=0
	self.hasRoot=False

    def __repr__(self,):
	return "__repr__ rootHash: %64x, total_leafs: %d" % (self.rootHash,self.leafcount)

    def Path(self,root,longest=True):
	"""
	Path computation function
	"""
	def argmax(lst1, lst2): return lst1 if len(lst1) > len(lst2) else lst2
	def argmin(lst1, lst2): return lst1 if len(lst1) < len(lst2) else lst2

	rightpath = []
       	leftpath = []
  	path = []
  	if root is None:
    	    return []
  	if (root.right is None) and (root.left is None):
    	    return [root.hash]
	elif root.right is not None:
	     rightpath = [root.hash] + self.Path(root.right,longest)
	elif root.left is not None:
             leftpath = [root.hash] + self.Path(root.left,longest)
	
	if longest:
		return argmax(rightpath, leftpath)
	else:
		return argmin(rightpath, leftpath)


    def createNode(self, data, isRoot=False):
        """
        Utility function to create a node.
        """
	self.leafcount += 1
        return Node(data,isRoot)

    def insert(self, node , data,isRoot=False):

	assert (isRoot == False or self.hasRoot == False), "Only one root"

	hash = sha256(data)

        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        if node is None:
	    #print "empty"
	    if isRoot == True:
		if self.hasRoot == False:
		    self.hasRoot = True
		    self.rootHash = hash

            return self.createNode(data,isRoot)
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
	#print node.hash,hash
	if node is None or node.hash == hash:
	    return node
        if node.hash < hash:
            return self.searchByHash(node.right, hash)
        else:
            return self.searchByHash(node.left, hash)

	
    def deleteNode(self,node,data):
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarion that we can handle
        Now it is handling only leaf.
        """
	return self.deleteNodeByHash(node,sha256(data))

    def deleteNodeByHash(self,node,hash):

	assert (node.isRoot == False),"Can not delete root leaf"
        
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

