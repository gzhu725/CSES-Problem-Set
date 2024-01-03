#we will use the fact that sum of all mumnbers 1 to n is (n * n + 1 )/ 2

n = int(input())
numbers = list(map(int, input().split()))
actual_sum = sum(i for i in range(1, n+1))
numbers_sum = sum(numbers)
print(actual_sum - numbers_sum)