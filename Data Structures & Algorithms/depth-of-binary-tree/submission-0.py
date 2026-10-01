# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([[root]])
        height = 0
        
        while q:
            cur_level = q.popleft()
            if cur_level:
                height += 1
                next_level =[]
                
                for i in range(len(cur_level)):
                    if cur_level[i].left:
                        next_level.append(cur_level[i].left)
                    if cur_level[i].right:
                        next_level.append(cur_level[i].right)

                q.append(next_level)

        return height





        