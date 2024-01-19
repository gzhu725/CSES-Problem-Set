n = int(input())
cubes = list(map(int, input().split(" ")))  # all cubes
current_top_min_values = [cubes[0]]  # represents the minimum value of the top cube in each tower

for i in range(1, n):
    if cubes[i] >= current_top_min_values[-1]:
        # we have a new tower
        current_top_min_values.append(cubes[i])
    else:
        # find the tower to stack on using binary search
        left, right = 0, len(current_top_min_values) - 1
        while left < right:
            mid = (left + right) // 2
            if current_top_min_values[mid] > cubes[i]:
                right = mid
            else:
                left = mid + 1

        # update the tower
        current_top_min_values[left] = cubes[i]

print(len(current_top_min_values))
