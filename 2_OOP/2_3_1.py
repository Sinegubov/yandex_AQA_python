class Cube:

    # напиши метод тут
    @staticmethod
    def get_cube_area(one_side_area):
        return one_side_area * 6

    def __init__(self, side_length, one_side_area):
        self.side_length = side_length
        self.area = self.get_cube_area(one_side_area)

print(Cube.get_cube_area(3))