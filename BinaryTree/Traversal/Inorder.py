# Iterative method
def inorderTraversal(self, root):
        result = []
        if not root:
            return result
        stack = []
        curr = root
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
            else:
                break
        return result