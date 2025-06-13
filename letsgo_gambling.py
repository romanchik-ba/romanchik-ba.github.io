import random
import re

# функция для проверки, является ли ввод целым числом
def is_integer(s: str) -> bool:
    pattern = r'^[+-]?\d+$'
    return bool(re.match(pattern, s))

# пользователь вводит ставку не менее 500
while True:
    user_input = input("Введите вашу ставку (не менее 500): ")
    
    if is_integer(user_input):
        money = int(user_input)
        if money >= 500:
            break
        else:
            print("Ставка должна быть не менее 500!")
    else:
        print("Некорректный ввод! Введите целое число.")
        
bet = money
symbols = [' 🍒 ', ' 🔔 ', ' 7️⃣ ']     # Список элементов для слотов
# Случайная генерация элeментов из списка symbols в список result
result = random.choices(symbols, k=3) 

# Первая итерация
if len(result) == 3 and result[0] == result[1] == result[2]: # Если все 3 элемента списка result одинаковы, то
    print(*result)
    win = max(1, int(bet * 0.10)) # Сохраняем сумму выигрыша (10% от bet)
    bet += win                          # Прибавляем сумму выигрыша в bet
    print(f'Ваш баланс: {int(bet)}')
    print(f"Поздравляем, Вы выиграли {int(win)}. Но Вы серьезно на этом остановитесь?")
else:
    print(*result)
    loss = max(1, int(bet * 0.20)) # Сохраняем сумму проигрыша (20% от bet)
    bet -= loss                         # Вычитаем сумму проигрыша из bet
    print(f'Ваш баланс: {int(bet)}')
    print(f"Вы проиграли {int(loss)}. Вы серьезно на этом остановитесь?")

# Далее запускается цикл
while bet >= 1:  # Цикл работает, пока баланс ≥ 1
    choice = input("Введите '+' чтобы продолжить игру или '-' чтобы выйти: ")
    
    if choice == '-':
        print("Вы решили остановиться. Игра окончена.")
        break
    elif choice == '+':
        
        # Здесь повторяем основной игровой блок
        result = (random.choices(symbols) + random.choices(symbols) + random.choices(symbols))
        
        if len(result) == 3 and result[0] == result[1] == result[2]: # Если все 3 элемента списка result одинаковы, то
            print(*result)
            win = max(1, int(bet * 0.20))  # Сохраняем сумму выигрыша (10% от bet)
            bet += win                  # Прибавляем сумму выигрыша в bet
            print(f'Ваш баланс: {int(bet)}')
            print(f"Поздравляем, Вы выиграли {int(win)}. Но Вы серьезно на этом остановитесь?")
        else:
            print(*result)
            loss = max(1, int(bet * 0.20)) # Сохраняем сумму проигрыша (20% от bet)
            bet -= loss                 # Вычитаем сумму проигрыша из bet
            print(f'Ваш баланс: {int(bet)}')
            print(f"Вы проиграли {int(loss)}. Вы серьезно на этом остановитесь?") 
        if bet <= 0:
            print("Ваш баланс обнулился. Игра окончена.")
            break
    else:
        print("Некорректный ввод. Пожалуйста, введите '+' или '-'.")
