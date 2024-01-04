n = int(input())
res = 0
cur_multiple = 5
while(cur_multiple <= n):
  occurrences = n // cur_multiple
  res += occurrences
  cur_multiple *=5
print(res)
#discrete math tldr: count the #s of multiples of 5 are in n