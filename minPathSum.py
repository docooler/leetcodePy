# Definition for a  binary tree node
import unittest

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
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
                    # print "start cols=1 sum = " + str(sum)
                    for x in xrange(rows):
                        # print "grid[" + str(x) + "][1] = " + str(grid[x][cols])
                        sum += grid[x][cols-1]
                    # print "start cols=1 sum = " + str(sum)
                else:
                    # print "rows : " + str(rows) + " cols :" + str(cols)
                    sum = min(pathSum(rows-1, cols)+grid[rows-1][cols-1], pathSum(rows, cols-1) + grid[rows-1][cols-1])

                # print "sumMap[(" + str(rows) + ", " + str(cols) + ")] = "  + str(sum)
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
        
               
