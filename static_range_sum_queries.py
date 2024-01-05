val = list(map(int, input().split()))
n = val[0]
q = val[1]
nums = list(map(int, input().split()))
#indexing is 1 based
res = ""
for i in range(q):
  vals = list(map(int, input().split()))
  a = vals[0]
  b = vals[1]
  s = sum(nums[a] for a in range(a-1, b))
  res += str(s) + ' '
print(res[:-1])