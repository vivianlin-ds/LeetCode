def maxSubarraySumK(nums: list[int], k: int) -> int:
    # Hashmap with prefix sum
    hashmap = {0: -1}
    max_length = 0
    current_sum = 0 

    for i in range(len(nums)):
        current_sum += nums[i]
        hashkey = current_sum - k

        if hashkey in hashmap.keys():
            length_subarray = i - hashmap[hashkey]
            max_length = max(length_subarray, max_length)
        if current_sum not in hashmap.keys():
            hashmap[current_sum] = i

    return max_length

if __name__ == "__main__":
    n1 = [1, -1, 5, -2, 3]
    k1 = 3
    n2 = [-2, -1, 2, 1]
    k2 = 1
    print(maxSubarraySumK(n1, k1))
    print(maxSubarraySumK(n2, k2))