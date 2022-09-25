class Square:
    def __init__(self, square):  # координаты квадрата
        self.y = square[0]
        self.x = square[1]
        self.status = True  # статус True - жив False - мёртв
        if self.x<0 or self.y<0:
            raise ValueError('координаты не могут быть отрицательными')

    def coords(self):
        return [self.get_y(),self.get_x()]

    def __str__(self):
        return str(self.y)+" "+str(self.x)
    def get_y(self):
        return self.y

    def get_x(self):
        return self.x

    def get_status(self):
        return self.status

    def destroy(self):
        self.status = False

    def get_neighborsquares(self):
        neighborsquares = []
        neighborsquares.append([self.y - 1, self.x])
        neighborsquares.append([self.y + 1, self.x])
        neighborsquares.append([self.y, self.x - 1])
        neighborsquares.append([self.y, self.x + 1])
        return neighborsquares