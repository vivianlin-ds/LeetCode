# Given root of binary tree. A ZigZag path for a binary tree is as defined: Choose any node in binary tree and a
# direction (right/left). If current direction is right, move to the right child of the current node, otheriwse,
# move to the left chile. Change the direction from right to left or from left to right. Repeat the second and third
# steps until you can't move. Zigzag length is defined as number of nodes listed - 1. Return longest ZigZag path
# contained in the tree.


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


def longestZigZag(root) -> int:
    max_length = [0]
    def zigzag(node, length, direction, max_length):
        max_length[0] = max(max_length[0], length)

        if node.left is not None:
            if direction != 'left':
                # Continue the zigzag path
                zigzag(node.left, length + 1, 'left', max_length)
            else:
                # Reset
                zigzag(node.left, 1, 'left', max_length)
        if node.right is not None:
            if direction != 'right':
                # Continue the zigzag path
                zigzag(node.right, length + 1, 'right', max_length)
            else:
                # Reset
                zigzag(node.right, 1, 'right', max_length)

    zigzag(root, 0, '', max_length)

    return max_length[0]


def main():
    print(longestZigZag(createTree([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1])))
    print(longestZigZag(createTree([1, 1, 1, None, 1, None, None, 1, 1, None, 1])))
    print(longestZigZag(createTree([1])))


if __name__ == '__main__':
    main()
