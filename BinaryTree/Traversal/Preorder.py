# Iterative preorder

def preorderTraversal(self, root):
        result = []
        parent = []
        ptr = root
        if not ptr:
            return result
        parent.append(ptr)
        while parent:
            rt = parent.pop()
            result.append(rt.val)
            if rt.right:
                parent.append(rt.right)
            if rt.left:
                parent.append(rt.left)
        return result
        
        
# recursive Preorder

def recursiveTraversal(self, root, result):
        if root:
            result.append(root.val)
            self.recursiveTraversal(root.left, result)
            self.recursiveTraversal(root.right, result)
        
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    self.recursiveTraversal(root, result)
    return result
