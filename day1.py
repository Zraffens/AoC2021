def increase(nums):
    counter = 0
    for i in range(len(nums) - 1):
        if i < len(nums) - 1 and nums[i] < nums[i+1] :
            counter += 1
    return counter


def increase_three(nums):
    counter = 0
    for i in range(len(nums) - 3):
        if sum(nums[i+1: i+4]) > sum(nums[i: i+3]):
            counter += 1
    return counter


with open('data.txt') as f:
    data = list(map(int, f.readlines()))

print(increase_three(data))
