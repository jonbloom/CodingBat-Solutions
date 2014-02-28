def big_diff(nums):
  big = nums[0]
  small = nums[0]
  for num in nums:
    small = min(num,small)
    big = max(num,big)
  return big-small
