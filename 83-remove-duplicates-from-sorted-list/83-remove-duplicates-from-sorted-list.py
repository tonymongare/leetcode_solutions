# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        
        if head is None:
            return None
        
        while current.next:
            if current.val == current.next.val:
                next_element = current.next.next
                current.next = next_element
            else:
                current = current.next
                
        return head
#end
