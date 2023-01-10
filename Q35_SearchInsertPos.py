# Question: Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# Constraints: nums contains distinct values sorted in ascending order.

def searchInsert(self, nums: list[int], target: int) -> int:
    # # For targets too small or too large
    # if target > nums[-1]:
    #     return len(nums)
    # elif target < nums[0]:
    #     return 0
    # # For targets within range of nums
    # else:
    #     for i, n in enumerate(nums):
    #         if n == target:
    #             return i
    #         elif n < target and nums[i+1] > target:
    #             return i + 1

    # Binary search
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def main():
    print(searchInsert(self=True, nums=[1, 3, 5, 6], target=5))
    print(searchInsert(self=True, nums=[1, 3, 5, 6], target=7))
    print(searchInsert(self=True, nums=[1, 3, 5, 6], target=2))
    print(searchInsert(self=True, nums=[1, 3, 5, 6], target=0))


if __name__ == '__main__':
    main()
