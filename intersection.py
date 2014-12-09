# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param two ListNodes
	# @return the intersected ListNode
	def getIntersectionNode(self, headA, headB):
		lenA = self.getListLength(headA)
		lenB = self.getListLength(headB)
		longHead = None
		shortHead = None
		lenDiff = 0

		if lenA == 0 or lenB == 0:
			return None

		if lenA > lenB:
			lenDiff = lenA - lenB
			longHead = headA
			shortHead = headB
		else:
			lenDiff = lenB - lenA
			longHead = headB
			shortHead = headA

		while lenDiff != 0:
			longHead = longHead.next
			lenDiff = lenDiff - 1

		if lenA == 1 or lenB == 1:
			if id(longHead) == id(shortHead):
				return longHead
			else:
				return None
				
		if longHead == shortHead:
		    return shortHead

		while shortHead.next != None:
			if id(shortHead.next) == id(longHead.next):
				return shortHead.next
			else:
				shortHead = shortHead.next
				longHead  = longHead.next
		return


	def getListLength(self, head):
		i = 0
		if head == None:
			return 0
		i = 1
		tmphead = head
		while tmphead.next != None:
			i = i + 1
			tmphead = tmphead.next

		return i