LC 21 - Merge Two Sorted Lists

Problem: You are given the heads of two sorted linked lists, list1 and list2.
Merge the two lists into one sorted list and return the head of the merged list.
The list should be made by splicing together the nodes of the first two lists.

Approach:
- Use a dummy node so the merged list's head does not need special handling.
- Keep a `current` tail pointer that starts at the dummy node.
- While both lists are non-empty, compare the head values. Attach the smaller
  node to `current.next` and advance that list's pointer. Move `current` along.
- Ties are resolved by taking from list1 first, which is stable but otherwise
  does not matter for the result.
- Once one list is exhausted, attach the remainder of the other list in one
  step; it is already sorted and already linked.
- Return `dummy.next`, skipping the sentinel node.

Time complexity: O(n + m) - every node in both lists is visited at most once,
where n and m are the lengths of list1 and list2.

Space complexity: O(1) extra space - only a dummy node and a few pointers are
allocated; the input nodes are relinked in place.
