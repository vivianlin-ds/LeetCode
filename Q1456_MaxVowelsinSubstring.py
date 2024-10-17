# Question: Given string s and int k, return max number of vowel letters in any substring of s with length k. String
# s is all lower case.

def maxVowels(s: str, k: int) -> int:
    vowels = set('aeiou')
    count = 0

    for i in range(k):
        if s[i] in vowels:
            count += 1

    max_vowel = count

    for i in range(k, len(s)):
        if s[i] in vowels:
            count += 1
        if s[i - k] in vowels:
            count -= 1
        max_vowel = max(max_vowel, count)

        if max_vowel == k:
            return k

    return max_vowel


def main():
    print(maxVowels('abciiidef', 3))
    print(maxVowels('aeiou', 2))
    print(maxVowels('leetcode', 3))
    print(maxVowels('a', 1))


if __name__ == '__main__':
    main()