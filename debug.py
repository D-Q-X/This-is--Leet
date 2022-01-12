class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        l1=ListNode(0)
        cur_l1=l1
        l2=ListNode(0)
        cur_l2=l2
        
        cur =head
        while cur.next!=None:
            if cur.val<x:
                cur_l1.next=cur
                cur_l1=cur_l1.next
            else:
                cur_l2.next=cur
                cur_l2=cur_l2.next
            cur=cur.next      
        cur_l1.next=l2.next
        return l1.next

sol=Solution()
print(sol.partition([1,4,3,2,5,2],3))