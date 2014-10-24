class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def minDepth(self, root):
        self.minDeep = None
        if root == None:
            return 0
        if root.left != None:
            self.treeDeepVisit(root.left, 1)
        if root.right != None:
            self.treeDeepVisit(root.right,1)

        if self.minDeep == None:
            return 1
        return self.minDeep

    def treeDeepVisit(self, root, parentDeep):
        selfDeep = parentDeep + 1
        if root.left == None and root.right == None:
            if self.minDeep != None:
                if self.minDeep > selfDeep:
                    self.minDeep = selfDeep
            else:
                self.minDeep = selfDeep
            return 
        if root.left != None:
            self.treeDeepVisit(root.left, selfDeep)
        if root.right != None:
            self.treeDeepVisit(root.right, selfDeep)
        
