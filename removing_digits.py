n = int(input())
res = 0
while n != 0:
  digits = list(str(n))
  n = min(n - int(d) for d in digits)
  res += 1
print(res)
