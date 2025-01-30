import random
import time
from data import *

def fight(player_number, current_enemy):
    round = random.randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]["hp"]
    print(f"Противник - {enemy['name']}: {enemy['script']}")
    input("Нажмите Enter, чтобы продолжить.")
    print()

    player = players[player_number]

    while player["hp"] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f"{player['name']} аттакует {enemy['name']}. ")
            crit = random.randint(1, 100)
            if crit < player["luck"]:
                enemy_hp -= player["attack"] * 3
            else:
                enemy_hp -= player["attack"]
            time.sleep(1)
            print(f"{player['name']} - {player['hp']}, {enemy['name']} - {enemy_hp}")
            print()
            time.sleep(1)
        else:
            print(f"{enemy['name']} аттакует {player['name']}. ")
            player["hp"] -= enemy["attack"] * player["armor"]
            time.sleep(1)
            print(f"{player['name']} - {player['hp']}, {enemy['name']} - {enemy_hp}")
            print()
            time.sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f"Противник - {enemy['name']}: {enemy['win']}")
        current_enemy += 1
    else:
        print(f"Противник - {enemy['name']}: {enemy['lose']}")
    player["hp"] = 100
    return current_enemy

def training(player_number):
    player = players[player_number]
    training_type = input("1 - тренировать атаку, 2 - тренировать оборону \nВаш выбор... ")
    for i in range(0, 101, 20):
        print(f"Тренировкка завершена на {i}%")
        time.sleep(1.5)
    if training_type == "1":
        player['attack'] += 2
        print(f"Тренировка окончена! Теперь атака равна {player['attack']}")
    elif training_type == "2":
        player["armor"] -= 0.09
        print(f"Тренировка окончена! Теперь броня поглощает {100 - player['armor']*100} урона")

def display_player(player_number):
    player = players[player_number]
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"]}ед.) равен {player["luck"]}')
    print(f'Броня поглощает {(1 - player["armor"]) * 100: .1f} % урона')


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Велична атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')

def shop(player_number):
    player = players[player_number]
    while True:
        print('Добро пожаловать, путник! Что хочешь приобрести?')
        print(f'У тебя есть {player["money"]} монет.')
        for key, value in items.items():
            print(f'{key} - {value["name"]}: {value["price"]}')
        item = input()
        if item in player['inventory']:
            print(f'У тебя уже есть {items[item]["name"]}')
        elif player['money'] >= items[item]['price']:
            print(f'Ты успешно приобрёл {items[item]["name"]}')
            player['inventory'].append(items[item]["name"])
            player['money'] -= items[item]['price']
        elif player['money'] == items[item]['price']:
            break 
        else:
            print('Не хватает монет :(')
            break
        print()
        print('Буду ждать тебя снова, путник!')
        print()
        break 

def display_inventory(player_number):
    player = players[player_number]
    print("У вас есть")
    for value in player['inventory']:
        print(value)
    print(f"У вас есть {player['money']} монет")
    print()
    if "Зелье удачи" in player['inventory']:
        potion =  input('Желаете выпить зелье удачи? \n1 - да, \n2 - нет')
        if potion == "1":
            player['luck'] += 7
            print(f"Готово, теперь удача вашего игрока равна {player['luck']}%")
            player['inventory'].remove("Зелье удачи")
    
                

def earn(player_number):
    player = players[player_number]
    print("Добро пожаловать на работу клоуном в цирке! У вас есть 66 процентов шанс заработать 500 монет или проиграть 500 монет")
    result = random.randint(1, 100)
    time.sleep(1.5)
    print("Результат...")
    time.sleep(1.5)
    print("Страшно?..")
    time.sleep(1.5)
    if result < 67:
        print("Молодец, так держать, мг-мг. (Повезло ему(ей)!) Возращайся еще))))")
        player['money'] += 500
    else:
        print("Молодец, так держать, cоветую оставаться таким же лохом!")
        player['money'] -= 500
    print(f"У вас осталось {player['money']} монет.")