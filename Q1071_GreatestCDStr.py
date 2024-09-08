# Question: Given strings s and t, t divides s iff s = t + t + ... + t. Return the largest string x such that x
# divides both given two strings. Given strings will be uppercase English letters.

def mgcdOfStrings(str1: str, str2: str) -> str:
    res = ""
    if str1 + str2 != str2 + str1:
        return res

    from math import gcd
    mgcd = gcd(len(str1), len(str2))
    res = str1[:mgcd]
    return res


def main():
    print(mgcdOfStrings('ABCABC', 'ABC'))
    print(mgcdOfStrings('ABABAB', 'ABAB'))
    print(mgcdOfStrings('LEET', 'CODE'))
    print(mgcdOfStrings('ABCDEF', 'ABC'))
    print(mgcdOfStrings('TAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX'))


if __name__ == '__main__':
    main()
