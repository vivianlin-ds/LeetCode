# Given root of binary tree, level of its root is 1m the level of its children is 2. Return the smallest level x suhc
# that sum of all values of ndoes at level x is maximal.


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


def maxLevelSum(root) -> int:
    curr_level, res_level = 1, 1
    max_sum = float('-inf')

    queue = [root]
    while queue:
        level_sum = 0
        for node in queue:
            level_sum += node.val

        if level_sum > max_sum:
            max_sum = level_sum
            res_level = curr_level

        # Set up queue to include nodes on the same level
        temp = []
        for node in queue:
            if node.right:
                temp.append(node.right)
            if node.left:
                temp.append(node.left)
        queue = temp

        curr_level += 1
    return res_level


def main():
    print(maxLevelSum(createTree([1, 7, 0, 7, -8, None, None])))
    print(maxLevelSum(createTree([989, None, 10250, 98683, -89388, None, None, None, -32127])))


if __name__ == '__main__':
    main()
