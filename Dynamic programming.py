def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Test
n = 10
print(fibonacci(n))  # 55

#Тодорхойлолт: Дэд асуудлуудын үр дүнг санах ойд хадгалж, дахин ашиглах замаар үр ашгийг нэмэгдүүлдэг.

#Жишээ: Fibonacci тооны дэс дарааллыг динамик программчлалаар олох: