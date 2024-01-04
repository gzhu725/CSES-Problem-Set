word = input()
s = set() #basically if the character is in the set, 2 occurences of the char have been seen, two ptr
i = 0
j = len(word) - 1
chars = [None] * len(word)
for char in word:
  if char in s:
    #second occurence
    chars[i] = char
    chars[j] = char
    i+=1
    j-=1
    s.remove(char)
  else:
    s.add(char)
if len(s) == 1:
  s = list(s)
  chars[i] = s[0]
if None in chars:
  print("NO SOLUTION")
else:
  print("".join(char for char in chars))


