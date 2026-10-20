import importlib.util
import os
import random


def _load(path, name):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(os.path.dirname(__file__), "..", path)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


module = _load(os.path.join("arrays", "LC_152.py"), "LC_152_module")
Solution = module.Solution


def max_product(nums):
    return Solution().maxSubArray(list(nums))


def brute_force(nums):
    """Reference O(n^2) oracle: the product of every non-empty subarray."""
    best = None
    for start in range(len(nums)):
        product = 1
        for end in range(start, len(nums)):
            product *= nums[end]
            if best is None or product > best:
                best = product
    return best


def test_leetcode_example_1():
    # Subarray [2, 3] has the largest product 6.
    assert max_product([2, 3, -2, 4]) == 6


def test_leetcode_example_2():
    # The whole array [0, 2] wins; the empty-product default of 0 is not the answer here.
    assert max_product([0, 2]) == 2


def test_leetcode_example_3():
    # The zero caps every run, so the best subarray is [0] itself. Neither -2 nor
    # the -2 * 0 pairing beats it, and the answer is not a lone negative either.
    assert max_product([-2, 0, -1]) == 0


def test_single_element():
    assert max_product([-3]) == -3


def test_even_length_negative_run_takes_the_whole_run():
    # Four negatives multiply to a positive 24, beating every shorter subarray.
    assert max_product([-4, -1, -2, -3]) == 24


def test_zero_blocks_the_negative_run_from_producing_a_product():
    # Every negative is cut off from the other by the zero, so no subarray with two
    # negatives exists and the best product is 0 rather than 4 or 24.
    assert max_product([-4, 0, -1]) == 0


def test_negative_run_grows_by_sign_flip():
    # cur_max alone would answer 3; the cur_min of -2 becomes 24 when times -4.
    assert max_product([-2, 3, -4]) == 24


def test_interior_zero_does_not_trap_the_scan():
    # A zero must not reset best, and the run after it must still be reachable.
    assert max_product([-2, -3, 0, -2, -3]) == 6


def test_positive_run_wins_over_singletons():
    # The -1 caps the run starting at 5, so the best product is the tail 7 * 8.
    assert max_product([5, 4, -1, 7, 8]) == 56


def test_zero_only_input():
    assert max_product([0]) == 0


def test_even_negative_prefix_then_positive_run():
    # [-2, -3, 4, 5] gives 120. Extending the three-negative prefix to five
    # elements flips the sign and would give -120, so best must be held, not
    # recomputed from the final element.
    assert max_product([-1, -2, -3, 4, 5]) == 120


def test_long_negative_run_of_even_length():
    # Four negatives give 120, beating the three-negative subarrays, which are
    # themselves negative products rather than merely smaller ones.
    assert max_product([-2, -3, -4, -5]) == 120


def test_matches_brute_force_on_exhaustive_small_inputs():
    # Every array of length <= 4 over {-2, -1, 0, 1, 2}, checked against the oracle.
    values = [-2, -1, 0, 1, 2]
    cases = [[]]
    for _ in range(4):
        cases = [prefix + [v] for prefix in cases for v in values]
    cases = [c for c in cases if c]

    for nums in cases:
        assert max_product(nums) == brute_force(nums), f"mismatch on {nums}"


def test_matches_brute_force_on_random_inputs():
    rng = random.Random(152)
    for _ in range(500):
        nums = [rng.randint(-4, 4) for _ in range(rng.randint(1, 12))]
        assert max_product(nums) == brute_force(nums), f"mismatch on {nums}"


def max_product_ignoring_the_running_min(nums):
    """Variant that tracks only the largest ending product, i.e. plain Kadane.

    Kept so the tests can show which inputs it gets wrong. It is *not* the
    solution: it has no way to recover a large product that only appears after a
    sign flip.
    """
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur * x)
        best = max(best, cur)
    return best


def test_running_min_is_load_bearing():
    # Without cur_min, [-2, 3, -4] collapses to 3 because -2 is thrown away
    # after it fails to beat 3. The real solution keeps -2 and turns it into 24.
    # This is the concrete reason cur_min exists, so it is asserted directly.
    assert max_product_ignoring_the_running_min([-2, 3, -4]) == 3
    assert max_product([-2, 3, -4]) == 24


def test_running_min_is_load_bearing_on_random_inputs():
    # The two variants may only agree by accident, so the disagreement is counted
    # rather than assumed: any input where they differ must be one where the
    # full solution matches the oracle and the reduced one does not.
    rng = random.Random(1521)
    disagreements = 0

    for _ in range(500):
        nums = [rng.randint(-4, 4) for _ in range(rng.randint(2, 12))]
        reduced = max_product_ignoring_the_running_min(nums)
        if reduced != max_product(nums):
            disagreements += 1
            assert reduced != brute_force(nums), f"reduced variant was right on {nums}"

    assert disagreements > 0, "expected the reduced variant to fail somewhere"


if __name__ == "__main__":
    test_leetcode_example_1()
    test_leetcode_example_2()
    test_leetcode_example_3()
    test_single_element()
    test_even_length_negative_run_takes_the_whole_run()
    test_zero_blocks_the_negative_run_from_producing_a_product()
    test_negative_run_grows_by_sign_flip()
    test_interior_zero_does_not_trap_the_scan()
    test_positive_run_wins_over_singletons()
    test_zero_only_input()
    test_even_negative_prefix_then_positive_run()
    test_long_negative_run_of_even_length()
    test_matches_brute_force_on_exhaustive_small_inputs()
    test_matches_brute_force_on_random_inputs()
    test_running_min_is_load_bearing()
    test_running_min_is_load_bearing_on_random_inputs()
    print("All tests passed for LC-152")