# Question: Given string s, reverse order of the words. A word is defined as sequence of non-space characters. Return
# string of words in reverse order concatenated by a single space.


def reverseWords(s: str) -> str:
    s_list = s.split()
    res = s_list[::-1]
    return ' '.join(res)


def main():
    print(reverseWords("the sky is blue"))
    print(reverseWords("   hello world"))
    print(reverseWords("a good      example"))


if __name__ == '__main__':
    main()
