n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
val = nums[n//2] #middle value to calculate lowest cost values
res = 0
for i in range(n):
  res += abs(nums[i] - val)
print(res)
