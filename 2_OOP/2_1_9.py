class Car:
    def calculate_travel_time(self, distance):
        return print(distance / 60)# замени эту строку на реализацию метода

class Bicycle:
    def calculate_travel_time(self, distance):
        return print(distance / 15)# замени эту строку на реализацию метода


car = Car()
bicycle = Bicycle()
car.calculate_travel_time(120)
bicycle.calculate_travel_time(45)
# вызови метод calculate_travel_time() для каждого экземпляра,
# передав в качестве параметра расстояние