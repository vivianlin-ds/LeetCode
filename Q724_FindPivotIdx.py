# Question: Given an int array nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index
# is equal to the sum of all the numbers strictly to the index's right.
# Return the leftmost pivot index. If no such index exists, return -1.


def pivotIndex(nums: list[int]) -> int:
    l_sum = 0
    r_sum = sum(nums)
    for i in range(len(nums)):
        r_sum -= nums[i]
        if l_sum == r_sum:
            return i
        l_sum += nums[i]
    return -1


def main():
    print(pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
    print(pivotIndex(nums=[1, 2, 3]))
    print(pivotIndex(nums=[2, 1, -1]))
    print(pivotIndex(nums=[-1, -1, -1, -1, -1, -1]))


if __name__ == '__main__':
    main()
