# Question: Strictly palindromic int is for every base b between 2 and n-2 (inclusive),
# the string representation of int in base b is palindromic.
# Given int n, return True/False.

def isStrictlyPalindromic(n: int):
    # Check every base.
    for b in range(2, n-1):
        res = []
        tmp = n
        while tmp:
            res.append(tmp % b)
            tmp //= b
        # Exit loop if not a palindrome.
        if res != res[::-1]:
            return False
    return True


def main():
    print(isStrictlyPalindromic(9))
    print(isStrictlyPalindromic(4))


if __name__ == '__main__':
    main()
