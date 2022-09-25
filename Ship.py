from Square import Square
class Ship:
    max_squares=3

    def strange_list(self): #короче, это список всех соседних клеток каждой клетки
        list = []
        for square in self.squares:
            list += square.get_neighborsquares()
        return list

    def ship_is_correct(self): #проверка, правильно ли собран корабль
        if len(self.squares)<=1:
            return True
        for square in self.squares:
            #print(square)
            if not(square.coords() in self.strange_list()):
                return False
        return True

    def get_status(self):
        return self.status

    def destroy(self):
        print('корабль уничтожен')
        for square in self.squares:
            if square.get_status()==True:
                print('топлю еще живую палубу')
                square.destroy()
        self.status=False

    def get_damage(self, square):
        square.destroy()
        for square_ in self.squares:
            if square_.get_status() == True:
                return True
        self.destroy()

    def __init__(self, squares_coordinates): #массив занимаемых клеток типа [[1,1],[1,2],[1,3]]
        self.status = True #статус True - жив False - мёртв
        self.squares = []
        for square_coordinates in squares_coordinates:
            square = Square(square_coordinates)
            self.squares.append(square)
        if not self.ship_is_correct():
            raise ValueError('корабль разорван!')

    def __str__(self):
        return "Корабль "+ str(len(self.squares))+ " клеток"