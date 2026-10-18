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
    print("All tests passed for LC-605")
