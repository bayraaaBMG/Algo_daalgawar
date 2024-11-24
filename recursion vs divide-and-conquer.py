def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test
print(factorial(5))  # 120

#1. Recursion vs Divide-and-Conquer
#Recursion нь асуудлыг өөртөө хандаж давтдаг. Divide-and-Conquer нь асуудлыг томоор хувааж шийдвэрлэдэг.

#Жишээ: Факториал олох рекурсив арга: