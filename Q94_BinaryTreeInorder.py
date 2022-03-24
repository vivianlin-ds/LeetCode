# Question: Given root of binary tree, return iorder traversal of its nodes' values

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversalrecur(root):
    """Recursive solution"""
    root = TreeNode(root)
    res = []

    if root:
        res += inorderTraversalrecur(root.left)
        res.append(root.val)
        res += inorderTraversalrecur(root.right)

    return res


# Follow up: Recursive solution is trivial, could you do it iteratively?
def inorderTraversaliter(root):
    """Iterative solution with stack"""
    root = TreeNode(root)
    res = []
    stack = []

    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            res.append(temp.val)
            root = temp.right

    return res


def main():
    print(inorderTraversalrecur(root=[1, None, 2, 3]))
    print(inorderTraversalrecur(root=[1, 2, 3, 4, 5, 6, 7]))
    print(inorderTraversalrecur(root=[]))
    print(inorderTraversaliter(root=[1, None, 2, 3]))
    print(inorderTraversaliter(root=[1, 2, 3, 4, 5, 6, 7]))
    print(inorderTraversaliter(root=[]))


if __name__ == '__main__':
    main()
