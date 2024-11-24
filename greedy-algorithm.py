def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1

# Test
coins = [1, 5, 10, 25]
amount = 63
print(coin_change(coins, amount))  # 6 (25+25+10+1+1+1)

#3. Greedy Algorithm
#Тодорхойлолт: Өгөгдсөн нөхцөлд хамгийн ашигтай буюу шууд үр дүнд хүрэх боломжит шийдлийг сонгодог алгоритм юм.

#Жишээ: Coin Change асуудал: