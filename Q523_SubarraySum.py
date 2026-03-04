def checkSubarraySum(nums: list[int], k: int) -> bool:
    # Ensure first element doesn't get returned True
    hashmap = {0: -1}
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]
        mod_k = current_sum % k 

        print(current_sum, mod_k, i, hashmap)
        if mod_k in hashmap.keys():
            index_diff = i - hashmap[mod_k]
            if index_diff >= 2:
                return True
        else:
            hashmap[mod_k] = i

    return False

if __name__ == "__main__":
    n1 = [23, 2, 4, 6, 7]
    k1 = 6
    
    n2 = [23, 2, 6, 4, 7]
    k2 = 13
    
    n3 = [5,0,0,0]
    k3 = 3
    print(checkSubarraySum(n1, k1))
    print(checkSubarraySum(n2, k2))
    print(checkSubarraySum(n3, k3))
