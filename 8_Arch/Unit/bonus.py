class BonusService:

    BASE_BONUS = 1000

    def calculate_bonus(self, productivity):
        bonus = self.BASE_BONUS + (productivity * 0.1)

        bonus_limit = 5000
        if bonus > bonus_limit:
            bonus = bonus_limit

        return bonus