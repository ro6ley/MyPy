import unittest


def min_max(nums):
    """
    Given five positive integers, find the minimum and maximum values
    that can be # calculated by summing exactly four of the five integers.

    Steps:
    - Find the maximum, minimum and sum of the numbers of the array.

    - Minimum value = sum - largest

    - Maximum value = sum - smallest
    """
    return "{} {}".format(sum(nums) - max(nums), sum(nums) - min(nums))


def remove_even(nums):
    """
    Remove the even numbers from a list and return the remainder
    """
    return [i for i in nums if i % 2 != 0]

print(min_max([2, 3, 1, 8, 4]))  # 10 17

print(min_max([1, 2, 3, 4, 5]))  # 10 14

print(remove_even([1, 2, 4, 6, 7]))  # [1, 7]


class RandomTests(unittest.TestCase):
    """
    Test the solutions
    """
    def test_min_max(self):
        self.assertEqual(min_max([2, 3, 1, 8, 4]), "10 17")
        self.assertEqual(min_max([1, 2, 3, 4, 5]), "10 14")

    def test_remove_even(self):
        self.assertEqual(remove_even([1, 2, 4, 6, 7]), [1, 7])


if __name__ == "__main__":
    unittest.main()
