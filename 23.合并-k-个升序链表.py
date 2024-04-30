#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # def mergeKLists(lists):
        #     head = point = ListNode(0)
        #     q = PriorityQueue()
        #     for l in lists:
        #         if l:
        #             # 由于 PriorityQueue 是基于元素的比较进行排序的，因此这里我们将链表节点的值和节点本身放入元组中
        #             # 元组的第一个元素是节点的值，用于比较；第二个元素是节点本身
        #             q.put((l.val, l))
        #     while not q.empty():
        #         val, node = q.get()
        #         point.next = node
        #         point = point.next
        #         node = node.next
        #         if node:
        #             q.put((node.val, node))
        #     return head.next
        
        # return mergeKLists(lists)

        def ifnotnull(nodelist:list):
            for nodes in nodelist:
                if nodes!=None:
                    return True
            return False
        
        head = ListNode()
        current_node = head
        temp_index = 0
        res = []
        while ifnotnull(lists):
        # 仍有非空node，即有剩余link list
            min = 99999
            # 找出最小节点
            for i in range(len(lists)):
                if lists[i]!=None:
                    if lists[i].val<min:
                        min = lists[i].val
                        # 记录要加入的节点
                        current_node.next = lists[i]
                        # 记录下标
                        temp_index = i
            # 最小节点所在链表往后读一个
            if lists[temp_index].next:
                lists[temp_index] = lists[temp_index].next
            else:
                lists[temp_index] = None
            # 目标链表往后读一个
            # print(current_node.next.val)
            current_node = current_node.next

        return head.next

            
# @lc code=end