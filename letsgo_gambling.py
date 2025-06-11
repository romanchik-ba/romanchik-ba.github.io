import random

# пользователь вводит ставку не менее 500
while True:  # Число money зачисляется в переменную-счетчик bet
    money = int(input("Введите вашу ставку (не менее 500): ")) 
    if money >= 500:  # Если число меньше 500, пользователь должен заново ввести число
        break
    print('Ставка должна быть не менее 500!')

bet = money
symbols = [' 🍒 ', ' 🔔 ', ' 7️⃣ ']     # Список элементов для слотов
# Случайная генерация элeментов из списка symbols в список result
result = (random.choices(symbols) + random.choices(symbols) + random.choices(symbols)) 

# Первая итерация
if len(result) == 3 and result[0] == result[1] == result[2]: # Если все 3 элемента списка result одинаковы, то
    print(*result)
    win = round(bet * 0.10, 3)          # Сохраняем сумму выигрыша (10% от bet)
    bet += win                          # Прибавляем сумму выигрыша в bet
    print(f'Ваш баланс: {int(bet)}')
    print(f"Поздравляем, Вы выиграли {int(win)}. Но Вы серьезно на этом остановитесь?")
else:
    print(*result)
    loss = round(bet * 0.20, 3)         # Сохраняем сумму проигрыша (20% от bet)
    bet -= loss                         # Вычитаем сумму проигрыша из bet
    print(f'Ваш баланс: {int(bet)}')
    print(f"Вы проиграли {int(loss)}. Вы серьезно на этом остановитесь?")

# Далее запускается цикл
while bet != 0:
    choice = input("Введите '+' чтобы продолжить игру или '-' чтобы выйти: ")
    
    if choice == '-':
        print("Вы решили остановиться. Игра окончена.")
        break
    elif choice == '+':
        
        # Здесь повторяем основной игровой блок
        result = (random.choices(symbols) + random.choices(symbols) + random.choices(symbols))
        
        if len(result) == 3 and result[0] == result[1] == result[2]: # Если все 3 элемента списка result одинаковы, то
            print(*result)
            win = bet * 0.10            # Сохраняем сумму выигрыша (10% от bet)
            bet += win                  # Прибавляем сумму выигрыша в bet
            print(f'Ваш баланс: {int(bet)}')
            print(f"Поздравляем, Вы выиграли {int(win)}. Но Вы серьезно на этом остановитесь?")
        else:
            print(*result)
            loss = bet * 0.20           # Сохраняем сумму проигрыша (20% от bet)
            bet -= loss                 # Вычитаем сумму проигрыша из bet
            print(f'Ваш баланс: {int(bet)}')
            print(f"Вы проиграли {int(loss)}. Вы серьезно на этом остановитесь?")   
# Полная остановка цикла в случае если переменная-счетчик bet достигла значения 0  
if bet == 0:
    print("Ваш баланс обнулился. Игра окончена.")