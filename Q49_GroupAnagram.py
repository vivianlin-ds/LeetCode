def groupAnagrams(strs: list[str]) -> list[list[str]]:
    from collections import Counter
    history = {}
    for str in strs:
        str_list = list(str)
        count = Counter(str_list)
        count_key = tuple(sorted(count.items()))
        if count_key not in history.keys():
            history[count_key] = [str]
        else:
            history[count_key].append(str)
    return list(history.values())

if __name__ == "__main__":
    s1 = ["eat","tea","tan","ate","nat","bat"]
    s2 = [""]
    s3 = ["a"]
    print(groupAnagrams(s1))
    print(groupAnagrams(s2))
    print(groupAnagrams(s3))