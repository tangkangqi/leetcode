class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preTraverse(root):
    '''
    前序便历
    :param root:
    :return:
    '''
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)

def midTraverse(root):
    """
    中序遍历
    :param root:
    :return:
    """
    if root == None:
        return
    preTraverse(root.left)
    print(root.value)
    preTraverse(root.right)

    