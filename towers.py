#2 ptr approach
i = 0 
j = 0 
towers = 0
n = int(input())
nums = list(map(int, input().split()))
while j < len(nums): 
  if nums[j] < nums[i]:
    #valid stack
    print('lol')
  else:
    #invalid stack
    towers+=1
    i = j
  j+=1
print(towers)
