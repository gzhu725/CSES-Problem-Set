#use the cross product of vectors formed by the line and the point in question. 
#If the cross product is positive, left
# if cross product negative, right
# if cross product 0, touching

t = int(input())
res = ""
for i in range(t):
  vals = list(map(int, input().split()))
  x1,y1,x2,y2,x3,y3 = [val for val in vals]
  cross_product = (x2-x1) * (y3-y1) - (y2-y1) * (x3-x1)
  if cross_product < 0:
    res += "RIGHT\n"
  elif cross_product > 0:
    res += "LEFT\n"
  else:
    res += "TOUCH\n"
print(res.strip())
