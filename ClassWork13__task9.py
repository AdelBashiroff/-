class Vector2D:
    type = 'Vector2D'
    count = 0

    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
        Vector2D.count += 1

    @property
    def x(self):
        return self.__x

    def add(self, other):
        if not isinstance(other, Vector2D):
            raise ValueError('Ожидается Vector2D')
        return Vector2D(self.__x + other.__x, self.__y + other.__y)

    def add2(self, other):
        self.__x += other.__x
        self.__y += other.__y

    @staticmethod
    def display_info():
        print(f'Это класс {Vector2D.type}. Кол-во созданных экземпляров класса: {Vector2D.count}')

    def __str__(self):
        return f'Vector: {self.__x}, {self.__y}'

if __name__ == '__main__':
    try:
        vector = Vector2D(5, 6)
        vector2 = Vector2D(2, 3)

        vector3 = vector.add(vector2)
        print(vector3)

        vector.add2(vector2)
        print(vector)

        Vector2D.display_info()

    except ValueError as e:
        print(e)
