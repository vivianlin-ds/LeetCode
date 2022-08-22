# Question: Happy number is a number that follows process:
# 1) Starts with any positive int, replace number by sum of the squares of its digits
# 2) Repeat process until number equals to 1 or loops endlessly in cycle which doesn't include 1.
# 3) Numbers ending in 1 are considered happy.

def isHappy(n):
    sums_seen = set()
    digits = str(n)
    while True:
        # Reset any existing sums.
        digit_sum = 0
        # Loop through each digit in the number passed in
        for num in digits:
            # Sum of squares of digits.
            digit_sum += int(num) ** 2
        # If sum has already been checked and not yet reached 1, number is not happy.
        if digit_sum in sums_seen:
            return False
        # Sum reaches 1, number is happy.
        elif digit_sum == 1:
            return True
        else:
            # Replace number with sum.
            digits = str(digit_sum)
            # Record the new sum.
            sums_seen.add(digit_sum)


def main():
    print(isHappy(19))
    print(isHappy(2))


if __name__ == '__main__':
    main()
