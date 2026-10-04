def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        required = target - nums[i]

        if required in seen:
            return [seen[required], i]

        seen[nums[i]] = i

    return []


nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)

print(result)