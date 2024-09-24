# Question: Given integer array of candies, each number representing number of candies the ith kid has and an
# integerextraCandies denote number of extra candies. Return bollean array of lenvgth n where result[i] is true if
# after giving the ith kid all the extraCandies, they will have the greatest number of candies among all kids,
# and false if otherwise. Multiple kids can have greatest number of candies.

def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    res = []
    max_num = max(candies)
    for num in candies:
        if num + extraCandies >= max_num:
            res.append(True)
        else:
            res.append(False)

    return res


def main():
    print(kidsWithCandies([2, 3, 5, 1, 3], 3))
    print(kidsWithCandies([4, 2, 1, 1, 2], 1))
    print(kidsWithCandies([12, 1, 12], 10))


if __name__ == '__main__':
    main()
