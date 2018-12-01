class Allergies(object):
    ALLERGENS = (
        'eggs',
        'peanuts',
        'shellfish',
        'strawberries',
        'tomatoes',
        'chocolate',
        'pollen',
        'cats',
    )

    def __init__(self, score):
        self.__lst = self.__process_score(score % 256)

    # I don't think using @property provides any value here.
    @property
    def lst(self):
        return self.__lst

    def is_allergic_to(self, item):
        return item in self.__lst

    # Can't take credit for using & because I copied the solution.
    # Don't know how else I could solve this without my old approach.
    def __process_score(self, score):
        """
        Credit goes to treyhunner on github for this approach using bitwise AND
        """
        return [
            item
            for i, item in enumerate(self.ALLERGENS)
            if score & 1<<i
        ]


