
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)




sol = Solution()


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print("Test Case 1 Output:", sol.isValidBST(root1))  


root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4, TreeNode(3), TreeNode(6))
print("Test Case 2 Output:", sol.isValidBST(root2))  


root3 = TreeNode(10)
root3.left = TreeNode(5)
root3.right = TreeNode(15, TreeNode(6), TreeNode(20))
print("Test Case 3 Output:", sol.isValidBST(root3))  
