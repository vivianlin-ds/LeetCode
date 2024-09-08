# Question: Given two strings, merge strings by adding letters in alternating order. If the string is longer than the
# other, append additional letters onto the end of the merged string.

def mergeAlternately(word1: str, word2: str) -> str:
    res = ""
    str_length = min(len(word1), len(word2))
    for i in range(str_length):
        res += word1[i]
        res += word2[i]

    if len(word1) > str_length:
        res += word1[str_length:]
    if len(word2) > str_length:
        res += word2[str_length:]

    return res


def main():
    print(mergeAlternately('abc', 'pqr'))
    print(mergeAlternately('ab', 'pqrs'))
    print(mergeAlternately('abcd', 'pq'))


if __name__ == '__main__':
    main()
