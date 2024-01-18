#logic and solution derived from https://codeforces.com/blog/entry/14516
#converted into python
#memoization and modulo...
F = {}

def f(n):
    if n in F:
        return F[n]
    
    k = n // 2
    if n % 2 == 0:
        F[n] = (f(k) * f(k) + f(k - 1) * f(k - 1)) % (10**9 + 7)
    else:
        F[n] = (f(k) * f(k + 1) + f(k - 1) * f(k)) % (10**9 + 7)
    
    return F[n]

if __name__ == "__main__":
    F[0] = F[1] = 1
    n = int(input())
    if n == 0:
        result = 0
    else:
      result = f(n - 1)
    print(result)
