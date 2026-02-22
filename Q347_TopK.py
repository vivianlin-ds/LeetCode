def topKFrequent(nums: list[int], k: int) -> list[int]:
    import heapq
    from collections import Counter

    heap = []
    count = Counter(nums)
    print(f"COUNT: {count}")
    
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        print(heap)
        if len(heap) > k:
            # Pop smallest frequency out to maintain only top k frequencies in the heap
            heapq.heappop(heap)
    return [num for freq, num in heap]


def topKFrequentBF(nums: list[int], k: int) -> list[int]:
    key_dict = {}
    for i in range(len(nums)):
        if nums[i] in key_dict:
            key_dict[nums[i]] += 1
        else:
            key_dict[nums[i]] = 1
    sorted_dict = sorted(key_dict.items(), key=lambda x: x[1], reverse=True)
    res = []
    for i in range(k):
        res.append(sorted_dict[i][0])
    return res


if __name__ == '__main__':
    n1 = [1,1,1,2,2,3]
    k1= 2
    n2 = [1]
    k2 = 1
    n3 = [1,2,1,2,1,2,3,1,3,2]
    k3 = 2
    print(topKFrequent(n1, k1))
    # print(topKFrequent(n2, k2))
    # print(topKFrequent(n3, k3))
    