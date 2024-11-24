def min_coins(coins, amount):
    memo = {}  

    def dp(rem):
        if rem < 0:
            return float('inf')  
        if rem == 0:
            return 0  
        if rem in memo:
            return memo[rem] 

        memo[rem] = min(dp(rem - coin) + 1 for coin in coins)
        return memo[rem]

    result = dp(amount)
    return result if result != float('inf') else -1  

# Unit test
def test_min_coins():
    # 3 coins (5 + 5 + 1)
    assert min_coins([1, 2, 5], 11) == 3
    assert min_coins([2], 3) == -1
    assert min_coins([1], 0) == 0

    print("All Ran 3 tests !")

# Run tests
test_min_coins()
