# Question: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting
# some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


def isSubsequence(s: str, t: str) -> bool:
    s_ch = 0
    for ch in t:
        if s_ch == len(s):
            return True
        if ch == s[s_ch]:
            s_ch += 1
    return s_ch == len(s)


def main():
    print(isSubsequence(s='a', t='ahbgdc'))
    print(isSubsequence(s='axc', t='ahbgdc'))
    print(isSubsequence(s='aec', t='abcde'))


if __name__ == '__main__':
    main()