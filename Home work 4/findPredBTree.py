def findPredecessorBTree(root, key):
    if not root.children:
        return findPredecessorBTree(root.children[key])
    elif key > 1:
        return root.keys[key - 1]
    else:
        curNode = root
        while True:
            if not curNode.parent:
                return None
            curParent = curNode.parent
            j = 1
            while curParent.children[j] != root:
                j += 1

            if j == 1:
                curNode = curParent
            else:
                return curParent.keys[j - 1]
