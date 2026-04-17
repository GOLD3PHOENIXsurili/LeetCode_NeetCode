# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(p,q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False
            
            return same(p.left,q.left) and same(p.right,q.right)
        
        def has_subtree(root):
            if not root:
                return False
            
            if same(root,subRoot):
                return True
            
            return has_subtree(root.left) or has_subtree(root.right)
        
        return has_subtree(root)




# serialization
# conerting all tree nodes and leaved into a string

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(root):
            if not root:
                return "#"
            return f",{root.val},{serialize(root.left)},{serialize(root.right)}"

        return serialize(subRoot) in serialize(root)





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        subtree_hashes = set()

        def hash_tree(node):
            if not node:
                return "null"
            
            left = hash_tree(node.left)
            right = hash_tree(node.right)

            h = f"{node.val},{left},{right}"
            subtree_hashes.add(h)
            return h

        # build hashes from root
        hash_tree(root)

        # separate function (no adding)
        def get_hash(node):
            if not node:
                return "null"
            
            left = get_hash(node.left)
            right = get_hash(node.right)

            return f"{node.val},{left},{right}"

        return get_hash(subRoot) in subtree_hashes