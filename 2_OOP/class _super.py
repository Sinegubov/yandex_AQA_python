class Tester:
    def __init__(self, name):
        self.name = name

    def test(self):
        return f"Тестировщик {self.name} проводит тестирование"
    
class Autotester(Tester):
    def __init__(self, name, tool):
        self.tool = tool
        super().__init__(name)
    def test(self):
        return f"Автотестировщик {self.name} проводит тестирование с помощью {self.tool}"

tester = Tester('Иван')
autotester = Autotester('Маша', 'Selenium')
print(tester.test())
print(autotester.test())