# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # bruteforce
        # vals = []
        # current = head
        # while current:
        #     vals.append(current.val)
        #     current = current.next
        # current = head
        # l = len(vals)
        # while l:
        #     v = vals.pop()
        #     current.val = v
        #     current = current.next
        #     l -= 1
        # return head
        #------------------------------------------------

        # Linked list reverse
        prev = None
        current = head
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev

        #---------------------------------------------------

        # recursion
        # if not head:
        #     return None
        
        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        #     head.next = None

        # return newHead


        
        