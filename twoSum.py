def twoSum(nums, target):
    pairs = []
    fullData = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append(i)
                pairs.append(j)
                data = pairs.copy()
                fullData.append(data)
                pairs.clear()
    print(fullData)

def twoSumMapWithoutDouble(nums, target):
    mapList = dict()
    for i, n in enumerate(nums):
        mapList[n] = i
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in mapList and i != mapList[diff]:
            return [i, mapList[diff]]


twoSum([1, 2, 3, 5, 9, 8, 3, 1], 4)        # [[0, 2], [0, 6], [2, 7], [6, 7]]
twoSum([2, 7, 11, 15], 9)   # [0, 1]
twoSum([3, 2, 4], 6)        # [1, 2]
twoSum([3, 3], 6)           # [0, 1]


twoSumMapWithoutDouble([1, 2, 3, 5, 9, 8], 4)
twoSumMapWithoutDouble([2, 7, 11, 15], 9)   # [0, 1]
twoSumMapWithoutDouble([3, 2, 4], 6)        # [1, 2]
twoSumMapWithoutDouble([3, 3], 6)           # [0, 1]