n = int(input("Введите  число n n ≥ 2 : "))

if n < 2:
    print("Число n должно быть больше или равно 2.")
else:
    previos_n = int(input("Введите целое число 1: "))
    for i in range(2, n + 1):
        current_n = int(input(f"Введите целое число 2: "))
        sum = previos_n + current_n
        print(sum)
        previos_n = current_n
