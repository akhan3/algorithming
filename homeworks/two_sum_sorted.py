import pytest


def two_sum_sorted(nums, target):
    print()
    # zero sum can always be produced with an empty subset
    # TODO: This is only true for group-sum but nor for two-sum problem
    if target == 0:
        return True

    # if len(nums) == 0:
    #     if target == 0:
    #         return True
    #     else:
    #         return False
    # if len(nums) == 1:
    #     if target == nums[0]:
    #         return True
    #     else:
    #         return False

    print("starting for loops...")
    for k1, N1 in enumerate(nums):
        if N1 == target:  # this check is not correct for two-sum problem
            return True
        nums2 = nums[k1 + 1 :]
        print(k1, nums, nums2)
        for k2, N2 in enumerate(nums):
            if N1 + N2 == target:  # this check is specific to two-sum problem
                return True
    return False


def main():
    return pytest.main(["-vxl", "--capture=no"])


if __name__ == "__main__":
    main()
