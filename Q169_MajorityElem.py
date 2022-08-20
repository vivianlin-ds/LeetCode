# Question: Find the majority element in a list of ints.
# Majority is defined as appearing more than n/2 times.

def majorityElement(nums):
    count = 0
    # Convert list to set to get all unique numbers.
    for number in set(nums):
        # Loop through the list to count occurrence of each unique number.
        for i in range(len(nums)):
            if number == nums[i]:
                count += 1
        # Determine if the number is a majority element, assuming there is only one majority number in each list.
        if count > len(nums) / 2:
            return number


def main():
    print(majorityElement([3, 2, 3]))
    print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(majorityElement([8, 8, 7, 7, 7]))


if __name__ == '__main__':
    main()
