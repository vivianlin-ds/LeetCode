# Question: Given root of BST, convert to Greater Tree such that every key of
# BST is plus sum of all keys greater than the original key in BST.
# BST: Left subtree of node contains only nodes with keys less than node's key,
# right subtree always greater than key and both left and right subtrees are also BST.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Get sum of right subtree in BST,
        # then inorder traversal (traverse to bottom/leaves left subtree, key, then right subtree.)
        self.total = 0

        def dfs(node):
            if node:
                dfs(node.right)
                self.total += node.val
                node.val = self.total
                dfs(node.left)

        dfs(root)
        return root


def main():
    pass


if __name__ == '__main__':
    main()
