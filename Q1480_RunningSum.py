# Question: Given an array nums. Running sum of an array is runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.


def runningSum(nums: list[int]) -> list[int]:
    res = []
    r_sum = 0
    for n in nums:
        r_sum += n
        res.append(r_sum)
    return res
    # # Faster solution
    # for i in range(1, len(nums)):
    #     nums[i] += nums[i-1]
    # return nums


def main():
    print(runningSum(nums=[1, 2, 3, 4]))
    print(runningSum(nums=[1, 1, 1, 1, 1]))
    print(runningSum(nums=[3, 1, 2, 10, 1]))


if __name__ == '__main__':
    main()
