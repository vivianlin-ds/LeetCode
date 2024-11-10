# Given root of binary tree and int targetSum, return the number of paths where the sum of the values along the path
# equals targetSum. Path does not need to start or end at the root or a leaf, but it must go downwards.

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


def pathSum(root, targetSum: int) -> int:
    prefix_sum = {0: 1}

    def dfs(node, running_sum):
        if node is None:
            return 0

        running_sum += node.val
        count = prefix_sum.get(running_sum - targetSum, 0)
        prefix_sum[running_sum] = prefix_sum.get(running_sum, 0) + 1
        # print(node.val, running_sum, count, prefix_sum)
        count += dfs(node.left, running_sum)
        count += dfs(node.right, running_sum)

        prefix_sum[running_sum] -= 1
        # print("COUNT", count)
        return count
    return dfs(root, 0)


def main():
    print(pathSum(createTree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8))
    print(pathSum(createTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22))


if __name__ == '__main__':
    main()
