# Question: Given int array gain of length n where gain[i] is net gain in altitude between points i and i + 1 for all
# (0 <= i < n). Return highest altitude of a point.

def largestAltitude(gain: list[int]) -> int:
    alt = [0]
    run_sum = 0
    for g in gain:
        run_sum += g
        alt.append(run_sum)
    return max(alt)


def main():
    print(largestAltitude([-5, 1, 5, 0, -7]))
    print(largestAltitude([-4, -3, -2, -1, 4, 3, 2]))


if __name__ == '__main__':
    main()
