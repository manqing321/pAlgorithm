# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printNode(node: TreeNode):
    lst = [node]
    while(len(lst) > 0):
        temp_lst = []
        while(len(lst)):
            ptr = lst.pop()
            print(ptr.val, end = " ")
            if ptr.left is not None:
                temp_lst.append(ptr.left)
            if ptr.right is not None:
                temp_lst.append(ptr.right)
        lst = temp_lst
        print("")

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find(node):
            if node is None:
                return 0, None
            deepl, nodel = find(node.left)
            deepr, noder = find(node.right)
            if deepl > deepr:
                return deepl + 1, nodel
            elif deepl < deepr:
                return deepr + 1, noder
            return deepr + 1, node
        return find(root)[1]

t7 = TreeNode(7)
t4 = TreeNode(4)
t2 = TreeNode(2, left=t7, right=t4)
t6 = TreeNode(6)
t5 = TreeNode(5, left=t6, right=t2)
t0 = TreeNode(0)
t8 = TreeNode(8)
t1 = TreeNode(1, left=t0, right=t8)
t3 = TreeNode(3, left=t5, right=t1)

ans = Solution().lcaDeepestLeaves(t3)
printNode(ans)