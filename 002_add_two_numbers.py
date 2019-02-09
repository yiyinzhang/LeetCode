'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

'''
the Definition of ListNode
'''

class ListNode(object):
	def __init__(self):
		self.val = None
		self.next = None
		
class ListNode_handle:
	def __init__(self):
		self.cur_node = None
		
	def add(self, data):
		node = ListNode()
		node.val = data
		node.next = self.cur_node
		self.cur_node = node
		return node
		
	def print_ListNode(self, node):
		while node:
			print '\nnode: ', node, ' value: ', node.val, ' next: ', node.next
			node = node.next
			
	def _reverse(self, nodelist):
		list = []
		while nodelist:
			list.append(nodelist.val)
			nodelist = node.next
		result = ListNode()
		result_handle = listNode_handle()
		for i in list:
			result = result_handle.add(i)
		return result
		
	def get_list(self, nodelist):
		list = []
		while nodelist:
			list.append(nodelist.val)
			nodelist = nodelist.next
		return list
		
'''
Solution1
'''
		
class Solution1(object):
	def addTwoNumbers(self, l1, l2):
		if not l1:
			return l2
		if not l2:
			return l1
		val1, val2 = [l1.val], [l2.val]
		while l1.next:
			val1.append(l1.next.val)
			l1 = l1.next
		while l2.next:
			val2.append(l2.next.val)
			l2 = l2.next
		num1 = ''.join([str[i] for i in val1[::-1]])
		num2 = ''.join([str[i] for i in val2[::-1]])
		tmp = str(int(num1) + int(num2))[::-1]
		res = ListNode(int(tmp[0]))
		run_res = res
		for i in range(1, len(tmp)):
			run_res.next = ListNode(int(tmp[i]))
			run_res = run_res.next
		return res

'''
Solution2
'''

class Solution2(object):
	def addTwoNumbers(self, l1, l2):
		if not l1 and not l2:
			return
		elif not (l1 and l2):
			return l1 or l2
		else:
			if l1.val + l2.val < 10:
				l3 = ListNode(l1.val + l2.val)
				l3.next = self.addTwoNumbers(l1.next, l2.next)
			else:
				l3 = ListNode(l1.val + l2.val - 10)
				l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next, ListNode(1)))
		return l3
		