n = int(input())
nums = list(map(int, input().split()))
positions = [-100] * (len(nums) + 1)
res = 1
for i in range(1,n):
  positions[nums[i]] = i #the index associated with each number
for i in range(1, n):
  cur = i
  next = i + 1
  if(positions[next]< positions[cur]):
    res+=1
print(res)


