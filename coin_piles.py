# gfg logic
# sum of the coins in both piles should be a multiple of 3.
# the size of the larger pile should not be more than twice the size of the smaller pile.
n = int(input())
res = ""
for i in range(n):
  a,b = list(map(int, input().split())) 
  res += "YES\n" if (a + b) % 3 == 0 and max(a,b) <= 2 * min(a,b) else "NO\n"
print(res.strip())