# Question: Given 0-indexed int array nums and int pivot, rearrange nums such that:
# Elements less than pivot are on the left side of pivot,
# Elements greater than pivot are on the right side of pivot,
# Relative order is maintained,


def pivotArray(nums: list[int], pivot: int) -> list[int]:
    lt, eq, gt = [], [], []
    for n in nums:
        if n < pivot:
            lt.append(n)
        elif n > pivot:
            gt.append(n)
        else:
            eq.append(n)
    return lt+eq+gt


def main():
    print(pivotArray(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10))
    print(pivotArray(nums=[-3, 4, 3, 2], pivot=2))


if __name__ == '__main__':
    main()
