def minWindow(s: str, t: str) -> str:
    # When length of t is greater than s, there is no solution
    if len(t) > len(s):
        return ""

    from collections import Counter
    t_count = Counter(list(t))
    left = 0
    current, target = 0, len(t_count)
    current_window = {keys: 0 for keys in t_count.keys()}
    min_array = float("inf")
    res = []
    for right in range(len(s)):
        if s[right] in current_window.keys():
            current_window[s[right]] += 1        
            if current_window[s[right]] == t_count[s[right]]:
                current += 1
        
        while current >= target:
            # Target is satisfied, now look for min subarray
            len_subarray = right - left + 1
            if len_subarray < min_array:
                min_array = len_subarray
                res = [left, right]

            if s[left] in current_window.keys():
                current_window[s[left]] -= 1
                if current_window[s[left]] < t_count[s[left]]:
                    current -= 1

            left += 1
    return s[res[0]:res[1]+1] if min_array != float("inf") else ""

if __name__ == '__main__':
    s1 = "ADOBECODEBANC"
    t1 = "ABC"

    s2 = "a"
    t2 = "a"

    s3 = "a"
    t3 = "aa"

    print(minWindow(s1, t1))
    print(minWindow(s2, t2))
    print(minWindow(s3, t3))
