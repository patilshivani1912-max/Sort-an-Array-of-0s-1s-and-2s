
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root == p or root == q:
            return root

        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        
        if left and right:
            return root

        
        return left if left else right

def buildTree(nodes):
    from collections import deque
    if not nodes: return None
    root = TreeNode(nodes[0])
    q = deque([root])
    i = 1
    while q and i < len(nodes):
        node = q.popleft()
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            q.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            q.append(node.right)
        i += 1
    return root

solution = Solution()

root = buildTree([3,5,1,6,2,0,8,None,None,7,4])
p = root.left            
q = root.left.right.right  
print(solution.lowestCommonAncestor(root, p, q).val)  

root = buildTree([3,5,1,6,2,0,8,None,None,7,4])
p = root.left            
q = root.right           
print(solution.lowestCommonAncestor(root, p, q).val)  

root = buildTree([1,2])
p = root                 
q = root.left            
print(solution.lowestCommonAncestor(root, p, q).val)
      
