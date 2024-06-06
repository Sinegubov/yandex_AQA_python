from bonus import BonusService

class TestBonusService:

    bonus = BonusService()

    def test_calculate_bonus_with_zero_productivity(self):
        actual = self.bonus.calculate_bonus(0)
        expected = 1000

        assert actual == expected

    def test_calculate_bonus_with_average_productivity(self):
        actual = self.bonus.calculate_bonus(1000)
        expected = 1000 + (1000 * 0.1)  # базовый бонус + 10% от производительности

        assert actual == expected