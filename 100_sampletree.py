class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def isSameTree(self, p, q):
        if 