# Question: Given root of binary tree, return preoder traversal of its nodes' values

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversalrecur(root):
    """Recursive solution"""
    root = TreeNode(root)
    res = []

    if root:
        res.append(root.val)
        res += preorderTraversalrecur(root.left)
        res += preorderTraversalrecur(root.right)

    return res


# Follow up: Recursive solution is trivial, could you do it iteratively?

def preorderTraversaliter(root):
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
    print(preorderTraversalrecur(root=[1, None, 2, 3]))
    print(preorderTraversalrecur(root=[1, 2, 3, 4, 5, 6, 7]))
    print(preorderTraversalrecur(root=[]))


if __name__ == '__main__':
    main()
