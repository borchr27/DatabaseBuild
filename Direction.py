class Direction:
    """A sample direction for a recipe class """

    def __init__(self, recipe, source, direc):
        self.recipe = recipe
        self.source = source
        self.direc = direc
    
    @property
    def item(self):
        return '{}.{}.{}'.format(self.recipe, self.source, self.direc)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.recipe, self.source, self.direc)