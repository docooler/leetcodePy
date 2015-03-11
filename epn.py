# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
import unittest

class Solution:
	# @param A, a list of integer
    # @return an integer
	def evalRPN(self, tokens):
		opStack = []
		for token in tokens:
			if token in ['+', '-', '*', '/']:
				op1 = (opStack.pop())
				op2 = (opStack.pop())
				if token is '+':
					op2 += op1
				elif token is '-':
					op2 -= op1
				elif token is '*':
					op2 *= op1
				elif token is '/': 
					op2 = int(op2*1.0/op1)
				opStack.append(op2)
			else: 
				opStack.append(int(token))
		return opStack[0]
			  
					

class SolutionUnitTest(unittest.TestCase):
	"""docstring for SolutionUnitTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testsingleNumber(self):
		# data = [0,1,3,2]
		s = Solution()

		# self.assertEqual(s.evalRPN(["2", "1", "+", "3", "*"]), 9)
		# self.assertEqual(s.evalRPN(["4", "13", "5", "/", "+"]), 6)
		self.assertEqual(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()
	# s = Solution()
	# s.grayCode(10)
