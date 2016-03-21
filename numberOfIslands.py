class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        self.mygrids = grid
        
        self.rows= len(grid)
        self.cols = len(grid[0])
        islands = 0
        for row in xrange(self.rows):
            for col in xrange(self.cols):
                if self.mygrids[row][col] == '1':
                    islands += 1
                    self.travelIsland(row, col)
        return islands
        
    def travelIsland(self, row, col):
        self.mygrids[row][col] ='2'
        
        if row-1>=0 and self.mygrids[row-1][col] == '1':
            self.travelIsland(row-1, col)
        if row+1 < self.rows and self.mygrids[row+1][col] == '1':
            self.travelIsland(row+1, col)
        if col-1>=0 and self.mygrids[row][col-1] == '1':
            self.travelIsland(row,col-1)
        if col+1< self.cols and self.mygrids[row][col+1] == '1':
            self.travelIsland(row,col+1)
            
                
