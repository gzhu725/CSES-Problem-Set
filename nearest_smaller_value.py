n = int(input())
nums = list(map(int, input().split()))
res = ""

def check_index(index, array):
  if(index == 0):
    return '0 '
  for i in range(index-1, -1, -1):
    if(array[i] < array[index]):
      return str(i + 1) + " "
  return '0 '


for i in range(n):
  res += check_index(i, nums)
print(res[:-1])