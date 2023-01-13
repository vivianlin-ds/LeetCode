# Question: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2,
# added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.


def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while left != right:
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        # Since array is sorted, last number will be largest. If still less than, then left needs to move.
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1


def main():
    print(twoSum(numbers=[2, 7, 11, 15], target=9))
    print(twoSum(numbers=[2, 3, 4], target=6))
    print(twoSum(numbers=[-1, 0], target=-1))
    print(twoSum(numbers=[0, 0, 3, 4], target=0))


if __name__ == '__main__':
    main()
