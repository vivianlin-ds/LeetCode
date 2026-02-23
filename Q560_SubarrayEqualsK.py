def subarraySum(nums: list[int], k: int) -> int:
    # Hashmap
    hashmap = {0: 1} # Initialize with prefix sum of 0 occuring once
    res = 0
    current_sum = 0

    for num in nums:
        current_sum += num
        hashkey = current_sum - k

        res += hashmap.get(hashkey, 0) # If hashkey exists, add the count of that prefix sum to result
        
        hashmap[current_sum] = hashmap.get(current_sum, 0) + 1 # Increment count of current prefix sum in hashmap
        
    return res
        


def subarraySumBF(nums: list[int], k: int) -> int:
    # Cannot use sliding window since nums can have negative

    count = 0
    rolling_sum = 0
    for i in range(len(nums)):
        rolling_sum = 0
        for j in range(i, len(nums)):
            rolling_sum += nums[j]
            if rolling_sum == k:
                count += 1

    return count

if __name__ == "__main__":
    n1 = [1,1,1]
    k1 = 2
    n2 = [1,2,3]
    k2 = 3
    print(subarraySum(n1, k1))
    print(subarraySum(n2, k2))
