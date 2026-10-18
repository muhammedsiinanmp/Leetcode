import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_605_module",
    os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_605.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def _can_place(flowerbed, n):
    """Run canPlaceFlowers() on a copy so callers keep their input intact."""
    return Solution().canPlaceFlowers(list(flowerbed), n)


def test_can_place_single_flower():
    assert _can_place([1, 0, 0, 0, 1], 1) is True


def test_can_place_two_flowers_impossible():
    assert _can_place([1, 0, 0, 0, 1], 2) is False


def test_can_place_zero_flowers_always_true():
    assert _can_place([1, 0, 0, 0, 1], 0) is True


def test_can_place_empty_bed_zero():
    assert _can_place([], 0) is True


def test_can_place_single_empty_plot():
    assert _can_place([0], 1) is True


def test_can_place_single_empty_plot_two_flowers():
    assert _can_place([0], 2) is False


def test_can_place_single_occupied_plot():
    assert _can_place([1], 1) is False


def test_can_place_adjacent_pair_only_one_flower():
    assert _can_place([0, 0], 1) is True
    assert _can_place([0, 0], 2) is False


def test_can_place_fills_gaps():
    assert _can_place([0, 0, 0, 0, 0], 3) is True
    assert _can_place([0, 0, 0, 0, 0], 4) is False


def test_can_place_uses_open_tail():
    assert _can_place([1, 0, 0], 1) is True


def _max_plant(flowerbed):
    """Exhaustive oracle: most flowers plantable in a bed of any small size."""
    length = len(flowerbed)
    state = list(flowerbed)
    best = 0

    def walk(index, planted):
        nonlocal best
        if index == length:
            best = max(best, planted)
            return
        walk(index + 1, planted)
        left_empty = index == 0 or state[index - 1] == 0
        right_empty = index == length - 1 or state[index + 1] == 0
        if state[index] == 0 and left_empty and right_empty:
            state[index] = 1
            walk(index + 1, planted + 1)
            state[index] = 0

    walk(0, 0)
    return best


def test_can_place_matches_exhaustive_oracle():
    import random

    for size in range(0, 13):
        for _ in range(20):
            bed = [random.randint(0, 1) for _ in range(size)]
            limit = _max_plant(bed)
            for n in range(0, size + 3):
                assert _can_place(bed, n) is (limit >= n), (bed, n, limit)


if __name__ == "__main__":
    test_can_place_single_flower()
    test_can_place_two_flowers_impossible()
    test_can_place_zero_flowers_always_true()
    test_can_place_empty_bed_zero()
    test_can_place_single_empty_plot()
    test_can_place_single_empty_plot_two_flowers()
    test_can_place_single_occupied_plot()
    test_can_place_adjacent_pair_only_one_flower()
    test_can_place_fills_gaps()
    test_can_place_uses_open_tail()
    test_can_place_matches_exhaustive_oracle()
    print("All tests passed for LC-605")
