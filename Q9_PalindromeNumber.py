# Question: An integer is a palindrome when it reads the same backward as forward.

def palindromestrs(self, x:int) -> bool:
    # Method with strings
    # Count the entire string backwards
    return str(x) == str(x)[::-1]


# Follow-up: Could you solve it without converting the integer to a string?
def isPalindrome(self, x: int) -> bool:
    # All negative numbers cannot be Palindrome
    if x < 0:
        return False

    # Need to keep the original x outside of loop
    x_initial = x

    # Construct the reverse x
    reverse = 0
    while x > 0:
        reverse = 10 * reverse + x % 10
        # Remove the last digit
        x = x // 10

    return reverse == x_initial


def main():
    print(palindromestrs(self=True, x=121))
    print(palindromestrs(self=True, x=-121))
    print(palindromestrs(self=True, x=100))
    print(isPalindrome(self=True, x=121))
    print(isPalindrome(self=True, x=-121))
    print(isPalindrome(self=True, x=100))


if __name__ == '__main__':
    main()
