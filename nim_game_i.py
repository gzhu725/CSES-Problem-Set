#this logic isn't original, but see the following video as to why XOR works 
#https://www.youtube.com/watch?v=coKE7qkYTL8

T = int(input())
for _ in range(T):
    n = int(input())
    res = 0
    vals = list(map(int, input().split())) 
    for j in range(n):
        res ^= vals[j]
    print('second' if res == 0 else 'first')
