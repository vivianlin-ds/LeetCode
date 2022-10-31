# Question: Given n person that are split into some unknown number of groups.
# Each person is labeled with unique ID from 0 to n-1.
# Given int array groupSizes, where groupSizes[i]: size of group that person i is in.
# Return list of groups such that each person i is in a group of size groupSizes[i].
# Each person should appear in exactly one group and every person must be in a group.


def groupThePeople(groupSizes: list[int]) -> list[list[int]]:
    group_dict = {}

    # Get the sizes of groups and the people in groups.
    for index, size in enumerate(groupSizes):
        if size not in group_dict:
            group_dict[size] = [index]
        else:
            group_dict[size].append(index)

    res = []
    # Iterate through the dictionary to get the desired result output.
    for key, val in group_dict.items():
        sub_ls = []
        # Iterate through val list (id of the people).
        for i in range(len(val)):
            if len(sub_ls) == key:
                res.append(sub_ls)
                sub_ls = []
            sub_ls.append(val[i])
        if sub_ls:
            res.append(sub_ls)

    return res


def main():
    print(groupThePeople([3, 3, 3, 3, 3, 1, 3]))


if __name__ == '__main__':
    main()
