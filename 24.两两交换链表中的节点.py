#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node1 = head
        node0 = ListNode()
        node0.next = node1
        node2 = node1.next
        node3 = node2.next
        # 当仍存在下两个节点时
        while node2:
            # 开头两个
            if head==node1:
                head = node2
                node2.next = node1
                node1.next = node3
            # 中间两个
            else:
                node0.next = node2
                node2.next = node1
                node1.next = node3

            if not node2.next or not node3 or not node3.next:
                break
            else:
                node0 = node2.next
                node1 = node2.next.next
                node2 = node1.next
                node3 = node2.next

        return head
# @lc code=end