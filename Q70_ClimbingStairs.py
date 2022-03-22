# Question: Takes n steps  to reach the top and each time can climb 1 or 2 steps
# How many distinct ways can be used to climb to the top?

def climbStairs(n: int) -> int:
    # Solution is Fibonacci numbers
    fibonacci = [1, 1]
    for i in range(2, n+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci[n]


def main():
    print(climbStairs(n=1))
    print(climbStairs(n=2))
    print(climbStairs(n=3))
    print(climbStairs(n=4))
    print(climbStairs(n=5))
    print(climbStairs(n=6))


if __name__ == '__main__':
    main()
