MOD = 10**9 + 7

def fib(n, a, b):
    if n == 0:
        a, b = 0, 1
        return
    x, y = 0, 0  # Initialize x and y here
    if n % 2 == 1:
        fib(n - 1, x, y)
        a, b = y, (x + y) % MOD
        return
    fib(n // 2, x, y)
    a = (x * (2 * y + MOD - x) % MOD) % MOD
    b = ((x * x) % MOD + (y * y) % MOD) % MOD
    return

if __name__ == "__main__":
    N = int(input())
    a, b = 0, 1
    fib(N, a, b)
    print(a)
