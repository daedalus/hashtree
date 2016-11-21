from merkle import Node,Tree

def main():
    root = None
    tree = Tree()
    root = tree.insert(root, "leaf: root")

    print root

    for i in range(0,20):
        print tree.insert(root, "leaf: %s" % i)

    print root


    print "Traverse Inorder"
    tree.traverseInorder(root)

    print "Traverse Preorder"
    tree.traversePreorder(root)

    print "Traverse Postorder"
    tree.traversePostorder(root)


if __name__ == "__main__":
    main()

