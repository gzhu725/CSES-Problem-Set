# see nim game i

def nim_sum(heaps):
    result = 0
    for heap in heaps:
        result ^= (heap%4)
    if result == 0:
        return "second\n"
    else:
        return "first\n"

# Input handling for multiple test cases
t = int(input())
res = ""
for _ in range(t):
    n = int(input())
    heaps = list(map(int, input().split()))
    res += nim_sum(heaps)
print(res.strip())
