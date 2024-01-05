n = int(input())
if n == 1:
  print(1)
  exit() 
nums = list(i for i in range(1, n+1))
if len(nums) <= 3:
  print("NO SOLUTION")
  exit()
if n % 2 == 0:
  evens = list(str(i) for i in range(2, n + 1) if i % 2 == 0)
  odds = list(str(i) for i in range(1, n) if i %2 != 0)
  print(" ".join(evens + odds))
  exit()
else:
  evens = list(str(i) for i in range(2, n) if i % 2 == 0)
  odds = list(str(i) for i in range(1, n + 1) if i %2 != 0)
  print(" ".join(evens + odds))
  exit()

#logic is posted on geeks for geeks
#basically every even number and every odd numbers difference has to be greater than 1
#so print the evens first and then the odds next