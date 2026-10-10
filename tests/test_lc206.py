import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_206_module",
    os.path.join(os.path.dirname(__file__), "..", "linked_lists", "LC_206.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
ListNode = module.ListNode
Solution = module.Solution


def build(values):
    """Build a linked list from a Python list and return its head."""
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_list(head):
    """Collect a linked list back into a Python list."""
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


def test_reverse_typical():
    assert to_list(Solution().reverseList(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]


def test_reverse_two_elements():
    assert to_list(Solution().reverseList(build([1, 2]))) == [2, 1]


def test_reverse_single_element():
    assert to_list(Solution().reverseList(build([7]))) == [7]


def test_reverse_empty_list():
    assert to_list(Solution().reverseList(build([]))) == []


def test_reverse_matches_python_oracle():
    """Cross-check the pointer walk against list(reversed(...))."""
    for size in range(0, 20):
        values = list(range(size))
        assert to_list(Solution().reverseList(build(values))) == values[::-1], size


def test_reverse_reuses_the_same_nodes():
    """Reversal must relink the existing nodes, not copy their values."""
    head = build([1, 2, 3])
    first, second, third = head, head.next, head.next.next

    reversed_head = Solution().reverseList(head)

    assert reversed_head is third
    assert to_list(reversed_head) == [3, 2, 1]
    assert third.next is second and second.next is first and first.next is None


if __name__ == "__main__":
    test_reverse_typical()
    test_reverse_two_elements()
    test_reverse_single_element()
    test_reverse_empty_list()
    test_reverse_matches_python_oracle()
    test_reverse_reuses_the_same_nodes()
    print("All tests passed for LC-206")
