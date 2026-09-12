import importlib.util
import os

# Import by file path to be robust to package/module names
spec = importlib.util.spec_from_file_location(
    "LC_2_module",
    os.path.join(os.path.dirname(__file__), '..', 'linked_lists', 'LC_2.py')
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
ListNode = module.ListNode
Solution = module.Solution


def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def test_add_two_numbers():
    s = Solution()
    # Test case 1: [2,4,3] + [5,6,4] = [7,0,8] (342 + 465 = 807)
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    result = s.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [7, 0, 8]
    
    # Test case 2: [0] + [0] = [0]
    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    result = s.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [0]
    
    # Test case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linked_list([9, 9, 9, 9])
    result = s.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]


if __name__ == "__main__":
    test_add_two_numbers()
    print("All tests passed for LC2")
