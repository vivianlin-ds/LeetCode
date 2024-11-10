# Given the root of a binary tree, return its max depth. Binary tree's max depth is number of nodes along longest
# path from the root node down to the farthest leaf node.


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


def printTree(root):
    if not root:
        return []

    tree = []
    nodes = [root]
    while nodes:
        current = nodes.pop(0)
        tree.append(current.val)
        if current.left:
            nodes.append(current.left)
        if current.right:
            nodes.append(current.right)
    return tree


def maxDepth(root) -> int:
    if not root:
        return 0
    left_subtree = maxDepth(root.left)
    right_subtree = maxDepth(root.right)
    return max(left_subtree, right_subtree) + 1


def main():
    print(maxDepth(createTree([3, 9, 20, None, None, 15, 7])))
    print(maxDepth(createTree([1, None, 2])))


if __name__ == '__main__':
    main()
