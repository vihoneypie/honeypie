from data import *
from helpers import *


name = input('''Выберите персонажа:
\n1 - Лиза
\n2 - Ксюша
\n3 - Нелля
\n4 - Денчик 
\n5 - Илиль 
\n6 - Антон
\n7 - Максим
\nВаш выбор...''')
player_number = int(name) - 1
current_enemy = 0

while True:
    action = input('''Выберите действие: 
    \n1 - атака 
    \n2 - тренировка 
    \n3 - информация о игроке 
    \n4 - информация о противнике 
    \n5 - инвентарь 
    \n6 - магазин 
    \n7 - пора на завод! 
    \n''')
    if action == "1":
        current_enemy = fight(player_number, current_enemy)
        if current_enemy == len(enemies):
            print("Вы всех смогли победить. ")
            break
    elif action == "2":
        training(player_number)
        print()
    elif action == "3":
        display_player(player_number)
        print()
    elif action == "4":
        display_enemy(current_enemy)
        print()
    elif action == '5':
        display_inventory(player_number)
        print()
    elif action == '6':
        shop(player_number)
        print()
    elif action == '7':
        earn(player_number)
        print()
print()
