# Given binary tree, find the lowest common ancestor of tow given nodes in the tree. Lowest common ancestor is
# defined between two nodes p and q as the lowest node in T that has both p and q as descendants. A node can be a
# descendant of itself. p and q will exist in the tree and will not equal each other. All node.val are unique.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    index = 1
    while index < len(values):
        node = queue.pop(0)
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


def lowestCommonAncestor(root, p, q):
    if root is None or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


def main():
    print(lowestCommonAncestor(createTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), TreeNode(5), TreeNode(1)))
    print(lowestCommonAncestor(createTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), TreeNode(5), TreeNode(4)))
    print(lowestCommonAncestor(createTree([1, 2]), TreeNode(1), TreeNode(2)))


if __name__ == '__main__':
    main()
