n = int(input())
ans = 1
for i in range(n):
  ans *= 2
  ans %= 1000000007
print(ans)