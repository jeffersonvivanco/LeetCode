def two_sum(nums, target):
    nums_map = {}
    for n in range(0, len(nums)):
        r = target - nums[n]
        if r in nums_map:
            sol = [nums_map[r], n]
            return sol
        else:
            nums_map[nums[n]]=n

print(two_sum([1, 2, 3], 5))