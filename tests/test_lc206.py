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


if __name__ == "__main__":
    test_reverse_typical()
    test_reverse_two_elements()
    test_reverse_single_element()
    test_reverse_empty_list()
    print("All tests passed for LC-206")
