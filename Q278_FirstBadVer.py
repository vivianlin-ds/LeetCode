# Question: Each version of product is developed based on the previous version,
# all the versions after a bad version are also bad.
# Suppose n versions [1, 2, ..., n], find the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.


def firstBadVersion(n: int) -> int:
    # Binary search
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        if left == right:
            if isBadVersion(left) is True:
                return left
        # Look to older versions for first bad version
        elif isBadVersion(mid) is True:
            right = mid
        # First bad version is a later version
        else:
            left = mid + 1
