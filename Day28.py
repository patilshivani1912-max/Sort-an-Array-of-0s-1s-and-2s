from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and \
                   isMirror(t1.left, t2.right) and \
                   isMirror(t1.right, t2.left)
        
        return isMirror(root.left, root.right)

def buildTree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root



test_cases = [
    [1, 2, 2, 3, 4, 4, 3],        
    [1, 2, 2, None, 3, None, 3],
    [1],                         
    [],                          
    [1, 2, 2, 3, None, None, 3]  
]

solution = Solution()

for i, case in enumerate(test_cases, 1):
    tree = buildTree(case)
    result = solution.isSymmetric(tree)
    print(f"Test Case {i}: Input = {case} → Output = {result}")
          
