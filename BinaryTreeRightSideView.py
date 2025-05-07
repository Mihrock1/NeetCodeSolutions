'''
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side 
of the tree, ordered from top to bottom.
'''

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        q = deque()
        q.append([root])

        while bool(q):
            level = q.popleft()
            # print(level)
            res.append(level[-1].val)
            newLevel = []

            for node in level:
                if node.left is not None:
                    newLevel.append(node.left)
                if node.right is not None:
                    newLevel.append(node.right)
            
            if bool(newLevel):
                q.append(newLevel)
            
        return res
