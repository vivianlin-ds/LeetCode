# Question: Given string, reverse only all the vowels in the string and return it.Vowels can appear in both lower or
# upper cases.


def reverseVowels(s: str) -> str:
    # new_s = [word for word in s]
    # vowels = 'aeiouAEIOU'
    # vowel_ind = []
    # for i in range(len(s)):
    #     if s[i] in vowels:
    #         vowel_ind.append(i)
    # s_vowel = []
    # vowel_ind.sort(reverse=True)
    # for ind in vowel_ind:
    #     s_vowel.append(s[ind])
    #     del new_s[ind]
    #
    # vowel_ind.sort(reverse=False)
    # i = 0
    # for ind in vowel_ind:
    #     new_s.insert(ind, s_vowel[i])
    #     i += 1
    #
    # return ''.join(new_s)

    vowels = 'aeiouAEIOU'
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            # Swap the vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return ''.join(s)


def main():
    print(reverseVowels("IceCreAm"))
    print(reverseVowels("leetcode"))
    print(reverseVowels("Haikyuu"))


if __name__ == '__main__':
    main()
