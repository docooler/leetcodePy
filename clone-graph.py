# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node == None:
            return None
        self.nodeMap = {}
        return self.cloneNode(node)
    def cloneNode(self, node):
        label = node.label
        if self.nodeMap.has_key(label):
            return self.nodeMap[label]
        n = UndirectedGraphNode(label)
        self.nodeMap[label] = n
        for x in node.neighbors:
            nei = self.cloneNode(x)
            n.neighbors.append(nei)
        return n
       
