#!/usr/bin/env python
# author Dario Clavijo 2016
# GPLv3
import time
from merkle import Node,Tree

def main():
    root = None
    tree = Tree()
    root = tree.insert(root, "leaf: root",isRoot=True)

    print "root"
    print tree
    print root

    for i in range(0,20):
        tree.insert(root, "leaf: %s" % i)

    print "Traverse Inorder"
    tree.traverseInorder(root)

    print "Traverse Preorder"
    tree.traversePreorder(root)

    print "Traverse Postorder"
    tree.traversePostorder(root)

    print "searchByHash 55008645c4762121a80a51cb14cfe3c441b54cfb027e24330451ae04dac4376b"
    print tree.searchByHash(root,int("55008645c4762121a80a51cb14cfe3c441b54cfb027e24330451ae04dac4376b",16))

    print "deleteNodeByHash"
    try:
    	print tree.deleteNodeByHash(root,int("55008645c4762121a80a51cb14cfe3c441b54cfb027e24330451ae04dac4376b",16))
    except:
	print "can not delete root leaf"

    print tree

    print "longestPath"
    print len(tree.Path(root))

    print "insertRoot"
    try:
    	tree.insert(root, "leaf: root",isRoot=True)
    except:
	print "Only one root"

    print "timing..."
    t0 = time.clock()
    for i in range(0,100000):
	last = tree.insert(root,"leaf %d" % i)
    t1 = time.clock()	
    delta = t1-t0
    print "ticks: %f CPU sec, %f sec per insert" % (delta,delta/100000)

if __name__ == "__main__":
    main()
