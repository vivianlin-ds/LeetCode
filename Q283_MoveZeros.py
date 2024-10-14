# Question: Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# # For purpose of checking, return original array.

def moveZeroes(nums: list[int]):
    first_zero_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[first_zero_pos] = nums[first_zero_pos], nums[i]
            first_zero_pos += 1
        # print(i, first_zero_pos, nums)
    return nums


def main():
    print(moveZeroes(nums=[0, 1, 0, 3, 12]))
    print(moveZeroes(nums=[0, 0, 0, 3, 12]))
    print(moveZeroes(nums=[0]))


if __name__ == '__main__':
    main()
