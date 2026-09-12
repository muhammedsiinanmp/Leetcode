class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two numbers represented as linked lists in reverse order.

        Traverse both lists simultaneously, adding digits with carry. Create new
        nodes for the result.
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            digit = total % 10
            carry = total // 10
            
            current.next = ListNode(digit)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
