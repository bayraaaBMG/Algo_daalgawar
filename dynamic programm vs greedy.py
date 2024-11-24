# Greedy Algorithm
def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1

# Dynamic Programming
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Test
coins = [1, 5, 10, 25]
amount = 63
print(coin_change_greedy(coins, amount))  # Greedy solution
print(coin_change_dp(coins, amount))  # Dynamic Programming solution

#3. Dynamic Programming vs Greedy
#Dynamic Programming бүх боломжит шийдлүүдийг тооцдог бол Greedy алгоритм тухайн үеийн хамгийн ашигтай шийдлийг сонгодог.

#Жишээ: Койн солилт: