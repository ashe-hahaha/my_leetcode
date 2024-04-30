#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodebefore = head
        node1 = head
        node2 = head
        for i in range(n-1):
            node2 = node2.next

        while node2.next:
            nodebefore = node1
            node1 = node1.next
            node2 = node2.next

        if node1 == head:
            head = head.next
        else:
            nodebefore.next = node1.next

        return head
    
# @lc code=end

