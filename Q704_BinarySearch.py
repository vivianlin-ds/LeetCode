# Question: Given an int array nums sorted in ascending order and an int target,
# write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# Must write an algorithm with O(log n) runtime complexity.


def search(nums: list[int], target: int) -> int:
    # Using for loop (didn't use the fact that array is sorted)
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i
    # return -1

    # Binary search method
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


def main():
    print(search(nums=[-1, 0, 3, 5, 9, 12], target=9))
    print(search(nums=[-1, 0, 3, 5, 9, 12], target=2))


if __name__ == '__main__':
    main()
