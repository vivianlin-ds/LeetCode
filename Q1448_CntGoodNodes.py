# Given binary tree root a node X in the tree is good if in the path from root to X, there are no nodes with value
# greater than X. Return the number of good nodes in the binary tree.


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


def goodNodes(root) -> int:
    stack = [(root, float('-inf'))]
    count = 0
    while stack:
        node, max_number = stack.pop()
        if node.val >= max_number:
            count += 1
        max_number = max(max_number, node.val)
        if node.left:
            stack.append((node.left, max_number))
        if node.right:
            stack.append((node.right, max_number))
    return count


def main():
    print(goodNodes(createTree([3, 1, 4, 3, None, 1, 5])))
    print(goodNodes(createTree([3, 3, None, 4, 2])))
    print(goodNodes(createTree([1])))


if __name__ == '__main__':
    main()
