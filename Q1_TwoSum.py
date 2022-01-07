def twoSum(self, nums: list[int], target: int) -> list[int]:
    # Question: Given an array of integers nums and an integer target,
    # return indices of the two numbers such that they add up to target.

    # Need to evaluate value and index, use dictionary
    hold = {}

    for i, values in enumerate(nums):
        remain = target - values

        if remain in hold:
            # Need to return the index of the numbers
            return [hold[remain], i]

        else:
            # Store 'values' as key and index 'i' as values
            hold[values] = i


def main():
    print(twoSum(self=True, nums=[2, 7, 11, 15], target=9))
    print(twoSum(self=True, nums=[3, 2, 4], target=6))
    print(twoSum(self=True, nums=[2, 4, 7, 12], target=16))


if __name__ == '__main__':
    main()
