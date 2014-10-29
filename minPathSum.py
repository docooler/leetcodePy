# Definition for a  binary tree node
import unittest

class Solution:
    def minPathSum(self, grid):
        sumMap = {}
        def pathSum(rows,cols):
            if (rows,cols) in sumMap:
                return sumMap[(rows, cols)]
            else:
                sum = 0
                flag = 0
                if rows == 1:
                    for x in xrange(cols):
                        sum += grid[rows-1][x]
                        flag = 1
                elif cols == 1 and flag != 1:
                    for x in xrange(rows):
                        sum += grid[x][cols-1]
                else:
                    sum = min(pathSum(rows-1, cols)+grid[rows-1][cols-1], pathSum(rows, cols-1) + grid[rows-1][cols-1])
                sumMap[(rows,cols)] = sum
                return sum 
        return pathSum(len(grid), len(grid[0]))

class SolutionTest(unittest.TestCase):
    """docstring for SolutionTest"""
    def setup(self):
        pass
    def tearDown(self):
        pass
    def testCase1(self):
        print "testCase1"
        s = Solution()
        grid = [[1,1]]
        
        self.assertEquals(s.minPathSum(grid), 2)
        grid = [[1,1],[1,2]]
        self.assertEquals(s.minPathSum(grid), 4)
        grid = [[1,2], [1,1]]
        self.assertEquals(s.minPathSum(grid), 3)
if __name__ == '__main__':
    unittest.main()
        
               
