seq = input()
cur_len = 0
longest = 0
i = 0
j = 0
while j != len(seq):
  if seq[i] != seq[j]:
    longest = max(cur_len, longest)
    cur_len = 0
    i=j
    #something
  else:
    cur_len += 1
    j+=1
if longest == 0 or cur_len > longest:
  longest = cur_len
print(longest)