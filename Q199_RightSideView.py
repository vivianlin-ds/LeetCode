# Given root of binary tree, return values of the nodes you can see ordered from top to bottom on the right side.


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


def rightSideView(root) -> list[int]:
    res = []
    if root is None:
        return res

    queue = [root]
    while queue:
        flag = False
        temp = []
        for node in queue:
            if flag is False:
                # Append the root of the tree
                res.append(node.val)
                flag = True
            if node.right:
                temp.append(node.right)
            if node.left:
                temp.append(node.left)
        queue = temp
    return res


def main():
    print(rightSideView(createTree([1, 2, 3, None, 5, None, 4])))
    print(rightSideView(createTree([1, None, 3])))
    print(rightSideView(createTree([])))


if __name__ == '__main__':
    main()
