def two_sum(nums, target):
    map = {}

    for i in range(0, len(nums)):
        if target - nums[i] in map.keys():
            return [map.get(target-nums[i]), i]

        else:
            map[nums[i]] = i
    return []


nums = [2, 11, 7, 15, 4]
target = 9

print(two_sum(nums, target))