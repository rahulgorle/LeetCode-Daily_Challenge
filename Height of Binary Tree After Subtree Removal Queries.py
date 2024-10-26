from collections import defaultdict
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Step 1: Record depth and height of each node
        depth = {}
        height = {}

        # DFS to compute depth and height
        def dfs(node, d):
            if not node:
                return -1
            depth[node.val] = d
            left_height = dfs(node.left, d + 1)
            right_height = dfs(node.right, d + 1)
            h = max(left_height, right_height) + 1
            height[node.val] = h
            return h

        dfs(root, 0)

        # Step 2: Max heights at each depth excluding the affected subtree
        max_height_at_depth = defaultdict(list)
        for node_val, d in depth.items():
            max_height_at_depth[d].append(height[node_val])

        # Sort and maintain two highest heights for each depth level
        max1_at_depth = {}
        max2_at_depth = {}
        for d, heights in max_height_at_depth.items():
            heights.sort(reverse=True)
            max1_at_depth[d] = heights[0]
            max2_at_depth[d] = heights[1] if len(heights) > 1 else -1

        # Step 3: Answer each query
        answer = []
        for q in queries:
            d = depth[q]
            if height[q] == max1_at_depth[d]:
                # Use the second highest if current node's height is the largest
                answer.append(max2_at_depth[d] + d)
            else:
                # If it's not the largest, just use the largest
                answer.append(max1_at_depth[d] + d)

        return answer
