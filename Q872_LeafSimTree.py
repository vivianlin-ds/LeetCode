# Given all leaves of a binary tree, from left to right order, values of the leaves form a leaf value sequence. Two
# binary trees are considered leaf-similar if their leaf value sequence is the sasme. Retrurn true iff two given trees
# with head nodes root1 and root2 are leaf-similar.

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


def leafSimilar(root1, root2) -> bool:
    leaves1, leaves2 = [], []

    def dfsLeaf(root, leaves):
        if root is None:
            return

        if root.left is None and root.right is None:
            leaves.append(root.val)

        dfsLeaf(root.left, leaves)
        dfsLeaf(root.right, leaves)

    dfsLeaf(root1, leaves1)
    dfsLeaf(root2, leaves2)
    print(leaves1, leaves2)
    return leaves1 == leaves2


def main():
    print(leafSimilar(createTree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
                      createTree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])))
    print(leafSimilar(createTree([1, 2, 3]), createTree([1, 3, 2])))


if __name__ == '__main__':
    main()
