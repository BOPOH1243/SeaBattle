from Board import Board
from Ship import Ship
import random

# board = Board()
# ship = Ship([[1, 1],[1, 2],[1, 3]])
# board.add_ship(ship)
# board.render()
# board.attack(1,1)
# board.attack(1,2)
# board.render(enemy=True)

enemy_board = Board()
for i in range(4):
    enemy_board.generate_random_ship()
    print("противник готов, генерация корабля", i)

player_board = Board()
print('твоя доска готова: ')



while player_board.get_count_of_ships() < 4:
    player_input = input(
        f'Вбей клетки корабля {player_board.get_count_of_ships() + 1} в формате 1,1 1,2 1,3 либо "r" чтобы создать рандомный корабль: ')


    def coord_is_valid(coord):
        if coord.isdigit():
            if int(coord) >= 0 and int(coord) < 6:
                return True
        return False


    if player_input == 'r':
        player_board.generate_random_ship()
        continue
    raw_coords = player_input.split(' ')
    coords = [element.split(',') for element in raw_coords]
    squares = []
    for coord in coords:
        if len(coord) == 2:
            if coord_is_valid(coord[0]) and coord_is_valid(coord[1]):
                squares.append([int(coord[0]), int(coord[1])])
            else:
                print('координаты неправильные')
                break
        else:
            print('координаты неправильные')
            break
    if len(squares)== len(coords):
        ship = Ship(squares)
        print('корабль', ship,'готов, добавляю')
        player_board.add_ship(ship)


def gena():
    while True:
        yield True
        yield False


for step in gena():
    print('_______________________________________')
    computer_coords = []
    print('твоя доска:')
    player_board.render()
    print('доска противника:')
    enemy_board.render(enemy=True)
    if step:
        while True:
            def coord_is_valid(coord):
                if coord.isdigit():
                    if int(coord) >= 0 and int(coord) < 6:
                        return True
                return False


            player_input = input('твой ход, координаты через пробел:')
            raw_coords = player_input.split(' ')
            if len(raw_coords) == 2:
                if coord_is_valid(raw_coords[0]) and coord_is_valid(raw_coords[1]):
                    attack_coords = [int(raw_coords[0]), int(raw_coords[1])]
                    print('координаты подтверждены', attack_coords)
                    enemy_board.attack(attack_coords[0], attack_coords[1])
                    break
                else:
                    print('координаты неправильные')
            else:
                print('координаты неправильные')
    else:
        print('ходит компьютер')
        coords = [random.randint(0,5),random.randint(0,5)]
        while coords in computer_coords:
            coords = [random.randint(0, 5), random.randint(0, 5)]
        player_board.attack(coords[0],coords[1])
        computer_coords.append(coords)
    if len(player_board.get_alive_ships_list())==0 or len(enemy_board.get_alive_ships_list())==0:
        winner = ''
        if step==True:
            winner='игрок'
        else:
            winner = 'компьютер'
        print('ну короче конец, победил ',winner)