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

        # using senitel linked list
        if not list1:
            return list2

        if not list2:
            return list1

        node = ListNode()
        curr = node

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2
            
        # while list1:
        #     curr.next = list1
        #     curr = curr.next
        #     list1 = list1.next

        # while list2:
        #     curr.next = list2
        #     curr = curr.next
        #     list2 = list2.next
        
        return node.next

        
        # curr = None
        # head = list1
        # if list1.val > list2.val:
        #     head = list2
        
        # while list1 or list2:
        #     if not list1:
        #         curr = list2
        #         curr.next = list2.next
        #     elif not list2:
        #         curr = list1
        #         curr.next = list1.next
        #     elif list1.val < list2.val:
        #         curr = list1
        #         curr.next = list1.next
        #     else:
        #         curr = list2
        #         curr.next = list2.next

        # return head
            


        