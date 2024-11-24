# Divide-and-Conquer (Recursive)
def fibonacci_dc(n):
    if n <= 1:
        return n
    return fibonacci_dc(n - 1) + fibonacci_dc(n - 2)

# Dynamic Programming (Memoization)
def fibonacci_dp(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_dp(n - 1, memo) + fibonacci_dp(n - 2, memo)
    return memo[n]

# Test
print(fibonacci_dc(10))  # 55
print(fibonacci_dp(10))  # 55

#2. Divide-and-Conquer vs Dynamic Programming
#Divide-and-Conquer дэд асуудлуудыг хадгалдаггүй, Dynamic Programming дэд асуудлуудыг санах ойд хадгалдаг.

#Жишээ: Fibonacci тоог Divide-and-Conquer болон Dynamic Programming аргаар олох: