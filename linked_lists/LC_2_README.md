LC 2 - Add Two Numbers

Problem: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Return the sum as a linked list.

Approach:
- Traverse both lists simultaneously, adding corresponding digits with carry.
- Create new nodes for each digit of the sum and link them.
- Handle remaining nodes if one list is longer, and continue propagating carry.

Time complexity: O(max(n, m)) where n and m are the lengths of the lists.
Space complexity: O(max(n, m)) for the result list.
