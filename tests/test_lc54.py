import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_54_module",
    os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_54.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_spiral_order():
    solution = Solution()

    assert solution.spiralOrder(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    ) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_spiral_order_rectangular():
    solution = Solution()

    assert solution.spiralOrder(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ]
    ) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def test_spiral_order_single_cell():
    solution = Solution()

    assert solution.spiralOrder([[42]]) == [42]


def test_spiral_order_single_row():
    solution = Solution()

    assert solution.spiralOrder([[1, 2, 3, 4]]) == [1, 2, 3, 4]


def test_spiral_order_single_column():
    solution = Solution()

    assert solution.spiralOrder([[1], [2], [3], [4]]) == [1, 2, 3, 4]


def test_spiral_order_two_by_two():
    solution = Solution()

    assert solution.spiralOrder(
        [
            [1, 2],
            [3, 4],
        ]
    ) == [1, 2, 4, 3]


def test_spiral_order_empty_matrix():
    solution = Solution()

    assert solution.spiralOrder([]) == []
    assert solution.spiralOrder([[]]) == []


if __name__ == "__main__":
    test_spiral_order()
    test_spiral_order_rectangular()
    test_spiral_order_single_cell()
    test_spiral_order_single_row()
    test_spiral_order_single_column()
    test_spiral_order_two_by_two()
    test_spiral_order_empty_matrix()
    print("All tests passed for LC-54")