# Question: Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

def maxSubArray(self, nums: list[int]) -> int:
    # Look at all the possible arrays in the list

    max_sum = 0

    for leftbound in range(0, len(nums)):
        current_sum = 0
        for rightbound in range(leftbound, len(nums)):
            current_sum += nums[rightbound]
            max_sum = max(current_sum, max_sum)
    return max_sum

def linearMaxSubarray(nums: list[int]) -> int:

# Follow-up: If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.


def main():
    print(maxSubArray(self=True, nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArray(self=True, nums=[1]))
    print(maxSubArray(self=True, nums=[5, 4, -1, 7, 8]))


if __name__ == '__main__':
    main()

