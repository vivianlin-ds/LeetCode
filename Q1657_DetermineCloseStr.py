# Question: Two strings are considered close if you can attain one from the other using following ops:
# Op1: Swap any two existing characters
# Op2: Transform every occurrence of one existing character into another existing chracter and do the same with the
# other character Operations can be used on either string as many times as necessary Given
# two strings word1 and word2, return true if word1 and word2 are close and false otherwise

def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) == len(word2):
        word1_dict = {}
        word2_dict = {}
        for i in range(len(word1)):
            if word1[i] in word1_dict.keys():
                word1_dict[word1[i]] += 1
            else:
                word1_dict[word1[i]] = 1
            if word2[i] in word2_dict.keys():
                word2_dict[word2[i]] += 1
            else:
                word2_dict[word2[i]] = 1
        keys = set(word1_dict.keys()) == set(word2_dict.keys())
        values = sorted(word1_dict.values()) == sorted(word2_dict.values())
        return keys and values
    return False


def main():
    print(closeStrings('abc', 'bca'))
    print(closeStrings('a', 'aa'))
    print(closeStrings('cabbba', 'abbccc'))


if __name__ == '__main__':
    main()
