# Question: A flowerbed in which some plots are planted and some are not, but cannot be planted in adjacent plots.
# Given int array containing 0's and 1's. Return true if n new flowers can be planted in the flowerbed without
# violating non-adjacent rule.

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:

    if n == 0:
        return True

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and \
                (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
    return False


def main():
    print(canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print(canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
    print(canPlaceFlowers([1, 0, 1, 0, 0], 1))


if __name__ == '__main__':
    main()
