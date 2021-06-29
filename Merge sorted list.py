class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        iterator=ListNode(-1)
        itr= iterator
        
        while(l1 and l2):
            if l1.val <= l2.val:
                itr.next=l1
                l1=l1.next
            else:
                itr.next=l2
                l2=l2.next
                
            itr=itr.next
        
        itr.next = l1 if l1 is not None else l2
        
                
        return iterator.next
                