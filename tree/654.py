# 654. 最大二叉树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        if len(nums) == 0: return None

        maxVal = float('-INF')
        index = 0
        for i in range(len(nums)):
            if nums[i] > maxVal:
                maxVal = nums[i]
                index = i
        root = TreeNode(maxVal)
        root.left = self.constructMaximumBinaryTree(nums[0:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root