def duplicate_nums(nums):
  return sorted([n for i, n in enumerate(nums) if n in nums[i+1:]]) or None


print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
# 3
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
# 72, 81, 99
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# None