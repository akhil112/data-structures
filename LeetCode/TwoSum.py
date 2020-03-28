
# source  = https://www.youtube.com/watch?v=gCin6Qz-eJQ

def twoSum(nums, target):
    temp = {}

    for i in range(len(nums)):
        comp = target-nums[i]

        if nums[i] in temp:
            print(nums[i], nums[temp[nums[i]]])
        else:
            temp[comp] = i


nums = [1, 4, 8, 3, 2, 9, 15]
target = 13
twoSum(nums, target)