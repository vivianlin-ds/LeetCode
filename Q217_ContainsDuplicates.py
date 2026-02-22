def containsDuplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)


if __name__ == "__main__":
    n1 = [1,2,3,1]
    n2 = [1,2,3,4]
    n3 = [1,1,1,3,3,4,3,2,4,2]
    
    print(containsDuplicate(n1))
    print(containsDuplicate(n2))
    print(containsDuplicate(n3))