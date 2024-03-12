class Tester:

    def __init__(self, name):
        self.name = name

    def work_hard(self, deadline):
        if deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')


tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)
