values = list(map(int, input().split()))
n = values[0]
x = values[1]
nums = list(map(int, input().split()))
original_indices = list(range(1, n + 1))  # Original indices from 1 to n
original_nums = list(zip(nums, original_indices))
original_nums.sort()  # Sort based on values

i = 0
j = n - 1

while i < j:
    cur_sum = original_nums[i][0] + original_nums[j][0]

    if cur_sum < x:
        i += 1
    elif cur_sum > x:
        j -= 1
    elif cur_sum == x:
        index1 = original_nums[i][1]
        index2 = original_nums[j][1]

        print(f"{index1} {index2}")
        exit()

print("IMPOSSIBLE")
