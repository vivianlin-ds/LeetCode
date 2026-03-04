def topKFrequent(words: list[str], k: int) -> list[str]:
    import heapq
    from collections import Counter
    word_count = Counter(words)
    heap = []
    for w, count in word_count.items():
        heapq.heappush(heap, (-count, w))
    
    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])
    return res


if __name__ == "__main__":
    w1 = ["i", "love", "leetcode", "i", "love", "coding"]
    k1 = 2

    w2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k2 = 4

    print(topKFrequent(w1, k1))
    print(topKFrequent(w2, k2))