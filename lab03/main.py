def bubble(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Меняем элементы местами
    return arr

n = int(input("Введите количество чисел: "))

numbers = []
for i in range(n):
    num = float(input(f"Введите число {i+1}: "))
    numbers.append(num)

order = input("Введите направление сортировки (возрастание/убывание): ").strip().lower()

if order == "возрастание":
    ascending = True
elif order == "убывание":
    ascending = False
else:
    print("Некорректный ввод. Сортировка по возрастанию по умолчанию.")
    ascending = True

sorted_numbers = bubble(numbers, ascending)

if ascending:
    print("Числа после сортировки по возрастанию:")
else:
    print("Числа после сортировки по убыванию:")

print(sorted_numbers)
