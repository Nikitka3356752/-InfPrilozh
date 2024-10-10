def eratosthen(n):
    primes = [True for _ in range(n + 1)]  # Создаем список с пометками всех чисел как простых
    p = 2  # Начинаем с первого простого числа

    while p * p <= n:
        # Если число простое, отмечаем все его кратные как составные
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]



N = int(input("Введите натуральное число N: "))

prime_numbers = eratosthen(N)

print(f"Простые числа до {N}: {prime_numbers}")
