# Question: Given array asteroids of int representing asteroids in a row. For each asteroid, absolute value represents
# its size and sign represents its direction ( + = right, - = left). Each asteroid moves at the same speed. Find out
# state of asteroids after all collisions. If two asteroids meet, smaller one will explode. If both aer the same
# size, both will explode. Two asteroids moving in the same direction will never meet.

def asteroidCollision(asteroids: list[int]) -> list[int]:
    res = []
    for a in asteroids:
        while res and a < 0 < res[-1]:
            if abs(a) > res[-1]:
                res.pop()
                continue
            elif abs(a) == res[-1]:
                res.pop()
            break
        else:
            res.append(a)
    return res


def main():
    print(asteroidCollision([5, 10, -5]))
    print(asteroidCollision([8, -8]))
    print(asteroidCollision([10, 2, -5]))


if __name__ == '__main__':
    main()
