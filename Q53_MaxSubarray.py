# Question: Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

def maxSubArray(nums: list[int]) -> int:
    current_sum = max_sum = nums[0]
    for number in nums[1:]:
        # Determine if next number is bigger than previous current_sum
        current_sum = max(number, current_sum + number)
        # Determine if max_sum needs to be updated
        max_sum = max(max_sum, current_sum)
    return max_sum


def main():
    print(maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArray(nums=[-2, -1]))
    print(maxSubArray(nums=[5, 4, -1, 7, 8]))
    print(maxSubArray(nums=[-1, 0, -2]))


if __name__ == '__main__':
    main()

