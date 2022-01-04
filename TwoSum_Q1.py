def twoSum(self, nums: list[int], target: int) -> list[int]:
    hold = {}
    for i, values in enumerate(nums):
        remain = target - nums[i]
        if remain in hold:
            return [hold[remain], i]
        else:
            hold[values] = i


def main():
    print(twoSum(self=True, nums=[2, 7, 11, 15], target=9))
    print(twoSum(self=True, nums=[3, 2, 4], target=6))
    print(twoSum(self=True, nums=[2, 4, 7, 12], target=16))


if __name__ == '__main__':
    main()
