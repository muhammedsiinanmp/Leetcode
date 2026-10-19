import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_21_module",
    os.path.join(os.path.dirname(__file__), "..", "linked_lists", "LC_21.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
ListNode = module.ListNode


def to_list(head: ListNode):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def from_list(values):
    if not values:
        return None
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def test_merge_two_lists_basic():
    list1 = from_list([1, 2, 4])
    list2 = from_list([1, 3, 4])
    result = Solution().mergeTwoLists(list1, list2)
    assert to_list(result) == [1, 1, 2, 3, 4, 4]


def test_merge_two_lists_one_empty():
    list1 = from_list([])
    list2 = from_list([0])
    result = Solution().mergeTwoLists(list1, list2)
    assert to_list(result) == [0]


def test_merge_two_lists_both_empty():
    list1 = from_list([])
    list2 = from_list([])
    result = Solution().mergeTwoLists(list1, list2)
    assert to_list(result) == []


if __name__ == "__main__":
    test_merge_two_lists_basic()
    test_merge_two_lists_one_empty()
    test_merge_two_lists_both_empty()
    print("All tests passed for LC-21")


def test_merge_two_lists_one_longer():
    list1 = from_list([1, 5, 10])
    list2 = from_list([2, 3])
    result = Solution().mergeTwoLists(list1, list2)
    assert to_list(result) == [1, 2, 3, 5, 10]


def test_merge_two_lists_matches_sorted_concatenation_oracle():
    """Cross-check against Python's sorted() over the combined values."""
    import random

    for _ in range(200):
        a = sorted(random.randint(-5, 5) for _ in range(random.randint(0, 8)))
        b = sorted(random.randint(-5, 5) for _ in range(random.randint(0, 8)))
        result = Solution().mergeTwoLists(from_list(a), from_list(b))
        assert to_list(result) == sorted(a + b), (a, b)


def test_merge_two_lists_reuses_nodes():
    """The merge should relink existing nodes, not copy their values."""
    list1 = from_list([1, 3])
    list2 = from_list([2, 4])
    result = Solution().mergeTwoLists(list1, list2)
    assert to_list(result) == [1, 2, 3, 4]


if __name__ == "__main__":
    test_merge_two_lists_basic()
    test_merge_two_lists_one_empty()
    test_merge_two_lists_both_empty()
    test_merge_two_lists_one_longer()
    test_merge_two_lists_matches_sorted_concatenation_oracle()
    test_merge_two_lists_reuses_nodes()
    print("All tests passed for LC-21")
