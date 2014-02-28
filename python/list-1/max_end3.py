def max_end3(nums):
  n = max(nums[0],nums[2])
  nums[0] = n
  nums[1] = n
  nums[2] = n
  return nums
