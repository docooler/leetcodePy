class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        self.dataMap = {}
        if root == None:
        	return []
        deep = self.treeDeepVisit(root, 0)
        result = []
        for i in xrange(deep+1):
        	values = self.dataMap[i]
        	if i%2 == 0:
        		values.reverse()
        	result.append(values)
        return result

    def treeDeepVisit(self, root, deepLevel):
    	if root == None:
    		return deepLevel -1

    	values = []
    	if self.dataMap.has_key(deepLevel):
    		values = self.dataMap[deepLevel]
    	values.append(root.val)
    	self.dataMap[deepLevel] = values

    	rightDeep = self.treeDeepVisit(root.right, deepLevel+1)
    	leftDeep  = self.treeDeepVisit(root.left,  deepLevel+1)
    	if rightDeep > leftDeep:
    		return rightDeep
    	return leftDeep
