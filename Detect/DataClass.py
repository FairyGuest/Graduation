class Point:
    def __init__(self, x, y, frame_size):
        self.x = x*frame_size[0]
        self.y = y*frame_size[1]


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mod(self):
        return (self.x**2+self.y**2)**0.5


class Angle:
    def __init__(self, name, data):
        self.name = name
        self.data = data

