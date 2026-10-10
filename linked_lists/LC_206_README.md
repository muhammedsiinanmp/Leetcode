LC 206 - Reverse Linked List

Problem: Given the head of a singly linked list, reverse the list and return
the new head.

Approach:
- Keep two pointers: `prev`, the already-reversed prefix (starts as None), and
  `current`, the node being processed (starts as the original head).
- Before overwriting `current.next`, stash it in `nxt` so the rest of the list
  is not lost.
- Flip `current.next` to point at `prev`, then slide both pointers forward:
  `prev` becomes `current` and `current` becomes `nxt`.
- When `current` falls off the end (None), `prev` is the last node visited,
  which is the new head of the reversed list.
- The nodes are relinked in place; no new nodes are allocated and the original
  node objects are reused.
