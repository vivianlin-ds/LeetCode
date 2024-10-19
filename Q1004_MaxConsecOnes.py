# Question: Given binary array nums and int k, return max number of consecutive 1's in the array if you can flip at
# most k 0's.


def longestOnes(nums: list[int], k: int) -> int:
    total_ones = 0
    left = 0
    zeros = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zeros += 1

        while zeros > k:
            # Need to move the window to the right
            if nums[left] == 0:
                zeros -= 1
            left += 1

        length = i - left + 1
        total_ones = max(length, total_ones)
    return total_ones


def main():
    print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))


if __name__ == '__main__':
    main()
