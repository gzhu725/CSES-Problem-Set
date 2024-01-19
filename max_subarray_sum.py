#leetcode 53 :), kadanes algorithm
n = int(input())
nums = list(map(int, input().split()))

max_sub = nums[0]
cur_sum = 0
for a in nums:
  if cur_sum < 0:
    cur_sum = 0
  cur_sum += a
  max_sub = max(max_sub, cur_sum)
print(max_sub)