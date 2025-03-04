'''
Given a binary search tree (BST) where all node values are unique, and two nodes from
the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that
both p and q as descendants. The ancestor is allowed to be a descendant of itself.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findAncestors(k: int, tree: TreeNode) -> list:
            if tree == None:
                return []

            if tree.val == k:
                return [tree]

            ancestors = findAncestors(k, tree.left) if tree.val > k else findAncestors(k, tree.right)

            if bool(ancestors):
                ancestors.append(tree)

            return ancestors

        p_ancestors = findAncestors(p.val, root)
        q_ancestors = findAncestors(q.val, root)

        if p in q_ancestors:
            return p

        if q in p_ancestors:
            return q

        p_ancestors_len = len(p_ancestors)
        q_ancestors_len = len(q_ancestors)

        longest_len = p_ancestors_len if p_ancestors_len >= q_ancestors_len else q_ancestors_len

        all_ancestors = set()

        for i in range(longest_len):
            if i in range(p_ancestors_len):
                if p_ancestors[i] not in all_ancestors:
                    all_ancestors.add(p_ancestors[i])
                else:
                    return p_ancestors[i]

            if i in range(q_ancestors_len):
                if q_ancestors[i] not in all_ancestors:
                    all_ancestors.add(q_ancestors[i])
                else:
                    return q_ancestors[i]
