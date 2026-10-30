# 4. Дано число k. Вычислите сумму 
# квадратов нечетных чисел от 
# 1 до k.

k = 10
summa = 0
for i in range(1, k + 1):
    if i % 2 != 0:
        summa += i ** 2
print(summa)
    
