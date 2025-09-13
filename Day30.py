def coinChange(coins, amount):
    
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  

    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1

print(coinChange([1, 2, 5], 11))  
print(coinChange([2], 3))         
print(coinChange([1], 0))         
              
