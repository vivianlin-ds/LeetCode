def isPalindrome(self, x: int) -> bool:
    # method with strings
    # return str(x) == str(x)[::-1]

    # method without strings
    # use while loop
    if x < 0:
        return False

    reverse = 0
    x_initial = x
    while x > 0:
        reverse = 10 * reverse + x % 10
        x = x // 10
    return reverse == x_initial


def main():
    print(isPalindrome(self=True, x=121))
    print(isPalindrome(self=True, x=-121))
    print(isPalindrome(self=True, x=100))


if __name__ == '__main__':
    main()
