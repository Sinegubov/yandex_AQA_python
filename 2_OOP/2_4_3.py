class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def create_margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def create_hawaiian(cls):
        return cls(['mozzarella', 'tomatoes', 'ananas', 'ham'])

print(Pizza.create_margherita().ingredients) # ['mozzarella', 'tomatoes']
print(Pizza.create_hawaiian().ingredients) # ['mozzarella', 'tomatoes', 'ananas', 'ham']