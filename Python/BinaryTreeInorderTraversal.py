# -*- coding: UTF-8 -*-
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree [1,null,2,3],
# 1
# \
# 2
# /
# 3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#
# Python, Python 3 all accepted.


class BinaryTreeInorderTraversal:

    # Recursive solution.
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     results = []
    #     if root is None:
    #         return results
    #
    #     if root.left is not None:
    #         results.extend(self.inorderTraversal(root.left))
    #
    #     results.append(root.val)
    #
    #     if root.right is not None:
    #         results.extend(self.inorderTraversal(root.right))
    #
    #     return results

    # Iterative solution.
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result

        stack = []
        while root is not None or len(stack) != 0:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack[len(stack) - 1]
            del stack[len(stack) - 1]
            result.append(root.val)
            root = root.right

        return result


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right

