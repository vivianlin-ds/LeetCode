def isAnagram(s: str, t: str) -> bool:
    from collections import Counter
    s_list = list(s)
    s_count = Counter(s_list)
    t_list = list(t)
    t_count = Counter(t_list)
    return s_count == t_count


if __name__ == "__main__":
    s1 = "anagram"
    t1 = "nagaram"
    s2 = "rat"
    t2 = "car"

    print(isAnagram(s1, t1))
    print(isAnagram(s2, t2))
