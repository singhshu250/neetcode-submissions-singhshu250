# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # bruteforce
        # store in arr, sort then put in linked list
        # vals = []
        # curr = list1
        # while curr:
        #     vals.append(curr.val)
        #     curr = curr.next
        
        # curr = list2
        # while curr:
        #     vals.append(curr.val)
        #     curr = curr.next
        
        # vals.sort()

        # dum = ListNode()
        # curr = dum

        # for v in vals:
        #     curr.next = ListNode(v)
        #     curr = curr.next

        # return dum.next

        #------------------------------------------------------
        # using senitel linked list
        # if not list1:
        #     return list2

        # if not list2:
        #     return list1

        # node = ListNode()
        # curr = node

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         curr.next = list1
        #         list1 = list1.next
        #     else:
        #         curr.next = list2
        #         list2 = list2.next
        #     curr = curr.next
        
        # curr.next = list1 or list2
        
        # return node.next

        
        # curr = None
        # head = list1
        # if list1.val > list2.val:
        #     head = list2
        
        #---------------------------------------------------

        #recursion method

        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        