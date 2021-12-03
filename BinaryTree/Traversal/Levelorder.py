# Level order
# sample answer : [[3],[9,20],[15,7]]
def levelOrder(self, root):
        result = []
        if not root:
            return result
        queue = []
        queue.append(root)
        while queue:
            iteration = len(queue)
            temp = []
            for i in range(iteration):
                ele = queue.pop(0)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                temp.append(ele.val)
            result.append(temp)
        return result