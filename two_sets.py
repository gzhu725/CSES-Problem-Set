
n = int(input())
s = (n * (n  + 1)) / 2
if s % 2 != 0:
  #odd sum, not possible for 
  print("NO")
else:
  one = set()
  two = set()
  if n % 2 == 0:
    #alternate
    i = 1
    j = n
    switch = False
    while i < j:
      if switch:
        two.add(i)
        two.add(j)
      else:
        one.add(i)
        one.add(j)
      switch = not switch
      i+=1
      j-=1
  else:
    #N is odd. fill up all the values whose sum is s // 2
    remainder = int(s // 2)
    for i in range(n, 0, -1):
      if i <= remainder:
        one.add(i)
        remainder -= i
      else:
        two.add(i)
  print("YES")
  print(len(one))
  print("".join(str(i) + " " for i in one))
  print(len(two))
  print("".join(str(i) + " " for i in two))