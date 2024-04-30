#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        head = ListNode()
        node3 = ListNode()
        head = node3

        while node1 and node2:
            if node1.val<=node2.val:
                node3.next = node1
                node3 = node3.next
                if node1.next:
                    node1 = node1.next
                else:
                    node1 = None
                    break
            else:
                node3.next = node2
                node3 = node3.next
                if node2.next:
                    node2 = node2.next
                else:
                    node2 = None
                    break    
        if node1:
            while node1.next:
                node3.next = node1
                node3 = node3.next
                node1 = node1.next
            node3.next = node1

        if node2:
            while node2.next:
                node3.next = node2
                node3 = node3.next
                node2 = node2.next
            node3.next = node2

        return head.next
                
# @lc code=end