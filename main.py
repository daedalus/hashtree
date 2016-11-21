from merkle import Node,Tree

def main():
    root = None
    tree = Tree()
    root = tree.insert(root, "leaf: root")
    root.isRoot = True

    print "root"
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
    try:
    	print "deleteNodeByHash"
    	print tree.deleteNodeByHash(root,int("55008645c4762121a80a51cb14cfe3c441b54cfb027e24330451ae04dac4376b",16))
    except:
	print "can not delete root leaf"

if __name__ == "__main__":
    main()
