from random import *
from Square import *
from Ship import Ship
import random


class Board:

    def __init__(self):
        self.ships = []
        self.size = 6
        self.ships_limit = 2

    def get_count_of_ships(self):
        return len(self.ships)

    def get_alive_ships_list(self):
        alive_ships=[]
        for ship in self.ships:
            if ship.get_status():
                alive_ships.append(ship)
        return alive_ships

    def very_strange_list(self): #список всех клеток, недоступных для занятия кораблём
        list = []
        for ship in self.ships:
            list += ship.strange_list()
        return list

    def attack(self, y, x):
        print(f'атака по{y} {x}')
        for ship in self.ships:
            for square in ship.squares:
                if square.coords() == [y, x]:
                    ship.get_damage(square)
                    print(y, x, 'попадание по', ship)
                    return True
        return False


    def add_ship(self, ship):
        for square in ship.squares:
            if square.coords() in self.very_strange_list():
                raise ValueError('корабль в запретной зоне')
        self.ships.append(ship)

    def render(self,enemy=False):
        vert_border_symbol='|'
        matrix = [['0' for i in range(self.size)] for i in range(self.size)]
        render_strings = []
        render_strings.append(vert_border_symbol.join(['E']+[str(i) for i in range(self.size)]))

        for ship in self.ships:
            for square in ship.squares:
                if square.get_status():
                    if not enemy:
                        matrix[square.get_y()][square.get_x()]='A'
                else:
                    matrix[square.get_y()][square.get_x()] = 'X'
        for i in range(len(matrix)):
            string = matrix[i].copy()
            string.insert(0, str(i))
            render_strings.append(vert_border_symbol.join(string))

        for e in render_strings:
            print(e)

    def generate_random_ship(self):
        squares = []

        def generate_startposition():
            return [randint(0, self.size-1), randint(0, self.size-1)]

        startposition = generate_startposition()
        while startposition in self.very_strange_list():
            startposition = generate_startposition()
        squares.append(Square(startposition))
        def generate_square():
            square_position = random.choice(squares[-1].get_neighborsquares())
            cooldown = 100
            flag = True
            it=0
            while (square_position in self.very_strange_list()) or (square_position[0]<0) or (square_position[0]>self.size-1) or (square_position[1]<0) or (square_position[1]>self.size-1) or (square_position in [square.coords() for square in squares]):
                square_position = random.choice(squares[-1].get_neighborsquares())
                it+=1
                if square_position[1]>=6 or square_position[0]>=6:
                    continue
                if it >cooldown:
                    flag = False
                    break
            if flag:
                squares.append(Square(square_position))
        generate_square()
        generate_square()
        ship = Ship([square.coords()for square in squares])
        self.ships.append(ship)




