import pytest

from miles import HobbitsPriorityStatus


class TestHobbitsPriorityStatus:

    # добавь параметризацию
    @pytest.mark.parametrize('miles, priority_status', [[299, 'Classic'], [300, 'Silver']])
    def test_add_miles_and_check_status(self, miles, priority_status):  # допиши параметры функции
        # создай нового хоббита в системе, добавь ему мили и проверь его статус
        hobbits_priority = HobbitsPriorityStatus()
        hobbit = 'Голлум'
        hobbits_priority.add_new_hobbit(hobbit)
        hobbits_priority.add_miles_to_hobbit(hobbit, miles)
        assert hobbits_priority.get_status(hobbit) == priority_status