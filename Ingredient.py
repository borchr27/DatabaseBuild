class Ingredient:
    """A sample ingredient class"""

    def __init__(self, recipe, ingredient, amt):
        self.recipe = recipe
        self.ingredient = ingredient
        self.amt = amt
    
    @property
    def item(self):
        return '{}.{}.{}'.format(self.recipe, self.ingredient, self.amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.recipe, self.ingredient, self.amt)