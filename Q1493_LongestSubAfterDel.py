# Question: Given binary array nums, delete one element from it and return size of longest non-empty subarray
# containing only 1's in the array. Return 0 if there is no such subarray.


def longestSubarray(nums: list[int]) -> int:
    total_ones = 0
    left = 0
    zeros = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zeros += 1

        while zeros > 1:
            # Need to move the window to the right
            if nums[left] == 0:
                zeros -= 1
            left += 1

        # Must delete one element from the array
        length = i - left
        total_ones = max(length, total_ones)
    return total_ones


def main():
    print(longestSubarray([1, 1, 0, 1]))
    print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
    print(longestSubarray([1, 1, 1]))


if __name__ == '__main__':
    main()
