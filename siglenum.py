class Solution:
	# @param A, a list of integer
    # @return an integer
	def singleNumber(self, A):
		return 7

class Solution_test:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        datamap = {}
        for i in A:
        	if datamap.has_key(i):
        		datamap[i] = 2
        	else:
        		datamap[i] = 1
        for (key, value) in datamap.items():
        	if value == 1:
        		return key

def main():
	data = [1,2,3,4,5,6,7,6,5,4,3,2,1]
	s = Solution()
	s_test = Solution_test()
	d_test = s_test.singleNumber(data)
	d = s.singleNumber(data)
	if d != d_test:
		print "Error"
	else:
		print "Done"

if __name__ == '__main__':
	main()