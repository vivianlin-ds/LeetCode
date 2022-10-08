# Question: Given array of ints nums, start with initial positive value startValue.
# In each iteration, calculate step by step sum of startValue plus elements in nums (from left to right).
# Return min positive value of startValue such that step by step sum is never less than 1.

def minStartValue(nums: list[int]) -> int:
    # Loop through list of numbers starting from second element.
    for i in range(1, len(nums)):
        # Replace the element as the sum of the previous two terms.
        nums[i] = nums[i] + nums[i-1]
    # Find the smallest step by step sum yielded.
    x = min(nums)

    if x > 0:
        return 1
    # If smallest step by step is less than 1, abs(x) + 1 = 1-x
    else:
        return 1-x


if __name__ == '__main__':
    print(minStartValue([-3, 2, -3, 4, 2]))
    print(minStartValue([1, 2]))
    print(minStartValue([1, -2, -3]))
    print(minStartValue([2, 3, 5, -5, -1]))
