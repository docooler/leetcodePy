import random
import unittest

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capa = capacity
        self.dic  = {}
        self.keyList = DList(capacity)
        self.keySet  = set()
    # @return an integer
    def get(self, key):
        if key in self.keySet:
            self.keyList.move2head(self.dic[key])
            return self.dic[key].value
        else:
            return -1
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.keySet:
            node = self.dic[key]
            node.value = value
            self.keyList.move2head(node)
        else:
            node = Node(key, value)
            ret = self.keyList.add(node)
            if ret != None:
                self.keySet.remove(ret.key)
                ret.value = -1
            self.dic[key] = node
            self.keySet.add(key)

class Node():
    """docstring for Node"""
    def __init__(self, key, value):
        self.value = value
        self.key   = key
        self.prev = None
        self.next = None
class DList(object):
    """docstring for DList"""
    def __init__(self, capacity):
        super(DList, self).__init__()
        self.capacity = capacity
        self.len      = 0
        self.head     = None
        self.tail     = None
    def add(self, node):
        self.insertFromHead(node)
        if self.len == self.capacity:
            return self.remmoveTail()
        else:
            self.len += 1
        return None

                
    def insertFromHead(self, node):
        if self.len == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
    def remmoveTail(self):
        deleNode = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return  deleNode


    def move2head(self, node):
        if node == self.head:
            return
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        node.next = self.head
        node.prev = None 
        self.head.prev = node
        self.head = node

        
class SolutionUnitTest(unittest.TestCase):
    """docstring for SolutionUnitTest"""
    def setup(self):
        pass
    def tearDown(self):
        pass
    def testsingleNumber(self):
        l = LRUCache(10)
        # for x in xrange(1,11):
        #   l.set(x,x)
        # for x in xrange(1,11):
        #   print str(x) + "=>" + str(l.get(x))
        # print "\n"
        # for x in xrange(11,20):
        #   l.set(x,x)
        #   print str(x) + "=>" + str(l.get(x))
        #   print str(x-10) + "=>" + str(l.get(x-10))
    def testcase2(self):
        print "testcase2"
        l = LRUCache(2)
        l.set(2,1)
        l.set(1,1)
        l.set(2,3)
        l.set(4,1)
        print l.get(1)
        print l.get(2)
    def testcast3(self):
        print "testcast3"
        l = LRUCache(2)
        l.set(2,1)
        l.set(2,2)
        print l.get(2)
        l.set(1,1)
        l.set(4,1)
        print l.get(2)
if __name__ == '__main__':
    unittest.main()
