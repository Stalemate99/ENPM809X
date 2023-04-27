def minBTree(root):
    if not root:
        return None
    elif not root.children:
        return root.key[0]
    else:
        return minBTree(root.children[0])