class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """Reverse a singly linked list and return the new head.

        Walk the list once, flipping each node's ``next`` to point at the
        previous node. ``prev`` trails one step behind and holds the new head
        once ``current`` falls off the end.
        """
        prev = None
        current = head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
