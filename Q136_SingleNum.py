# Question: Given non-empty array of ints where every element appears twice except for one. Find the single element.

def singleNumber(nums):
    for i in range(len(nums)):
        # Remove the specific index and check if number continue to exist in list.
        target = nums[i]
        nums.remove(target)
        if target not in nums:
            return target
        else:
            nums.insert(i, target)


def singleNumberXOR(nums):
    target = 0
    for i in nums:
        # Since each element appears twice, can use XOR operator to identify elements without a pair.
        target ^= i
    return target


def main():
    print(singleNumber([2, 2, 1]))
    print(singleNumber([4, 1, 2, 1, 2]))
    print(singleNumber([1]))
    print(singleNumberXOR([2, 2, 1]))
    print(singleNumberXOR([4, 1, 2, 1, 2]))
    print(singleNumberXOR([1, 1, 3, 3, 3]))


if __name__ == '__main__':
    main()
