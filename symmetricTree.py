
class Solution:
    # @param s, a string
    # @return a boolean
    def isSymmetric(self, root):
        stack = []
        if root == None:
            return True
        stack.append((root.left, root.right))
        while stack != []:
            left, right = stack.pop()
            if left == None and right == None:
                continue
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            else:
                stack.append((left.right, right.left))
                stack.append((left.left, right.right))
        return True
