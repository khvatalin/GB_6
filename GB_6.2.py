class Road:
    __length = None
    __width = None
    weigth = None
    thickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Создать дорогу')

    def intake(self):
        self.weigth = 25
        self.thickness = 0.05
        summ = self.length * self.width * self.weigth * self.thickness / 1000
        print(f'Нужно {summ} тонн для строительства')

road_to_village = Road(5000, 3)
road_to_village.intake()