# Question: Deci-binary number is a decimal number with each of 0 or 1 digits but no leading zeros.
# Given string n that represents a positive deicmal int, return min number of positive deci-binary number needed
# so that they sum up to n.

def minPartitions(n: str) -> int:
    res = n[0]
    for i in range(1, len(n)):
        res = max(n[i], res)
    return res


# Optimized solution
def opt_minPartitions(n: str) -> int:
    return int(max(n))


def main():
    print(minPartitions("1"))
    print(minPartitions("32"))
    print(minPartitions("82734"))
    print(minPartitions("27346209830709182346"))
    print(opt_minPartitions("1"))
    print(opt_minPartitions("32"))
    print(opt_minPartitions("82734"))
    print(opt_minPartitions("27346209830709182346"))


if __name__ == '__main__':
    main()
