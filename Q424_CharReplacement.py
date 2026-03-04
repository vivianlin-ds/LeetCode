def characterReplacement(s: str, k: int) -> int:
    left = 0
    longest_repeat = max_freq = 0
    counter = {}
    for right in range(len(s)):
        if s[right] not in counter:
            counter[s[right]] = 1
        else:
            counter[s[right]] += 1
        max_freq = max(max_freq, counter[s[right]])
        
        while (right - left + 1) - max_freq > k:
            counter[s[left]] -= 1
            left += 1

        longest_repeat = max(longest_repeat, (right - left + 1))

    return longest_repeat

if __name__ == '__main__':
    s1 = "ABAB"
    k1 = 2

    s2 = "AABABBA"
    k2 = 1

    print(characterReplacement(s1, k1))
    print(characterReplacement(s2, k2))
