severity_list = ['Блокирующий', 'Критический', 'Значительный', 'Незначительный', 'Тривиальный']

class BugDefinition:

        def __init__(self, priority, severity):
                self.priority = priority
                self.severity = severity

        # метод определяет, подходящее ли число указано в качестве приоритета бага
        @staticmethod
        def is_right_priority(priority):
                if 0 < priority < 5:
                        return True
                return False

        # метод определяет, входит ли указанное значение критичности
        # в список возможных значений
        @staticmethod
        def is_right_severity(severity):
                if severity not in severity_list:
                        return False
                return True

# с помощью функции определяем, можно ли создать объект бага и распределить его разработчику
def add_bug(priority, severity):
        bug = None
        if BugDefinition.is_right_priority(priority) and BugDefinition.is_right_severity(severity):
                bug = BugDefinition(priority, severity)
        return bug

# распределяем баг по разработчикам в зависимости от его критичности и приоритета
def submit_bug_to_developer(bug):
        if bug and bug.priority >= 4 and bug.severity in ['Блокирующий', 'Критический']:
                return 'Передано Senior Developer'
        elif bug and 4 > bug.priority >= 2 and bug.severity in ['Значительный', 'Незначительный']:
                return 'Передано Middle Developer'
        elif bug:
                return 'Передано Junior Developer'
        return 'Распределение невозможно'

# задаём неправильные параметры
bug = add_bug(10, 'Высокий')
print(submit_bug_to_developer(bug)) # Распределение невозможно