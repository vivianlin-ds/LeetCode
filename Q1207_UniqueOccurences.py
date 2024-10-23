# Question: Given array of int arr, return true if number of occurrences of each value in array is unique or false
# otherwise

def uniqueOccurrences(arr: list[int]) -> bool:
    track = {}
    for num in arr:
        if num in track.keys():
            track[num] += 1
        else:
            track[num] = 1
    unique_num = len(set(arr))
    unique_occur = len(set(track.values()))
    return unique_num == unique_occur


def main():
    print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))
    print(uniqueOccurrences([1, 2]))
    print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))


if __name__ == '__main__':
    main()
