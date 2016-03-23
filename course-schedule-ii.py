class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.nodepCourses = []
        self.prerequisites = prerequisites
        self.courseSerials = [[]]*numCourses
        serials =[]
        for num in xrange(numCourses):
            self.loopList = []
            if self.isCourseCycle(num) == True:
                return []
            while self.loopList != []:
                course = self.loopList.pop()
                if course not in serials:
                    serials.append(course)
        return serials
                        
    def isCourseCycle(self, num):
        if num in self.nodepCourses:
            return False
        if num in self.loopList:
            return True
        self.loopList.append(num)
        for pre in self.prerequisites:
            if num == pre[0]:
                ret =  self.isCourseCycle(pre[1])
                if ret == True:
                    return True
        self.nodepCourses.append(num)
        return False
