from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total = 0
    for n in nums:
        total += n
    return total

def get_min(nums: List[int]) -> int:
    mini = nums[0]
    for n in nums:
        if n < mini:
            mini = n
    return mini

def get_max(nums: List[int]) -> int:
    maxi = nums[0]
    for n in nums:
        if n > maxi:
            maxi = n
    return maxi

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
