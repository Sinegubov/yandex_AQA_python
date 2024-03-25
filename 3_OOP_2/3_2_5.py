class RobotVacuum:
    def __init__(self, state):
        self.__state = state

    @property                   # геттер для свойства state
    def state(self):
        return self.__state

    @state.setter              # сеттер для свойства state
    def state(self, state):
        if state in ["работает", "заряжается", "в ожидании"]:
            self.__state = state
        else:
            print(f"Недопустимое состояние: {state}. Состояние может быть 'работает', 'заряжается' или 'в ожидании'")
# создали объект
robo_vacuum = RobotVacuum("в ожидании")

# обратились к свойству, чтобы получить состояния
print(robo_vacuum.state)  # Вывод: в ожидании

# перезаписали свойство, чтобы установить состояние
robo_vacuum.state = "работает"
print(robo_vacuum.state)  # Вывод: работает

# попытались использовать свойство, чтобы установить недопустимое состояние
robo_vacuum.state = "летает"  # Вывод: Недопустимое состояние: летает. Состояние может быть 'работает', 'заряжается' или 'в ожидании'
print(robo_vacuum.state)   # Вывод: работает 
