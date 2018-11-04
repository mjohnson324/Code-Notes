from collections import OrderedDict
# Use to associate scores with allergies and maintain order for processing
ALLERGENS = OrderedDict()
ALLERGENS[128] = "cats"
ALLERGENS[64] = "pollen"
ALLERGENS[32] = "chocolate"
ALLERGENS[16] = "tomatoes"
ALLERGENS[8] = "strawberries"
ALLERGENS[4] = "shellfish"
ALLERGENS[2] = "peanuts"
ALLERGENS[1] = "eggs"

class Allergies(object):
    def __init__(self, score):
        self._score = score % 256
        self._lst = self._process_score(self._score)

    def is_allergic_to(self, item):
        return True if item in self._lst else False

    # Don't know why @property is useful here. Is it so the list can't be
    # tampered with once set?
    @property
    def lst(self):
        return self._lst

    def _process_score(self, score):
        known_allergies = []
        for rating, allergen in ALLERGENS.items():
            if score == 0:
                break
            if score >= rating:
                known_allergies.append(allergen)
                score -= rating
        return known_allergies


