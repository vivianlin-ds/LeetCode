# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Question says do not return anything, modify in-place.
# For purpose of checking, return original array.


def rotate(nums: list[int], k: int):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums


def main():
    print(rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
    print(rotate(nums=[-1, -100, 3, 99], k=2))


if __name__ == '__main__':
    main()
