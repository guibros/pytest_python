from math import exp
from typing import Dict


# typage par Lin
class Fuzzy:
    @classmethod
    def sigmoid(cls, x: float):
        return 1 / (1 + exp(-x))

    @classmethod
    def fuzzify(cls, budget: int):
        ret: Dict[str, float] = {'Very Low': 0, 'Low': 0, 'Medium': 0, 'High': 0, 'Very High': 0}
        if budget < 300:
            ret['Very Low'] = 1.0
        elif 300 <= budget < 400:
            ret['Very Low'] = 1.0
            ret['Low'] = Fuzzy.sigmoid((budget - 400) / 100)
        elif 400 <= budget < 500:
            ret['Very Low'] = Fuzzy.sigmoid((500 - budget) / 100)
            ret['Low'] = Fuzzy.sigmoid((budget - 400) / 100)
        elif 500 <= budget < 600:
            ret['Very Low'] = Fuzzy.sigmoid((500 - budget) / 100)
            ret['Low'] = 1.0
        elif 600 <= budget < 700:
            ret['Low'] = 1.0
            ret['Medium'] = Fuzzy.sigmoid((budget - 700) / 100)
        elif 700 <= budget < 800:
            ret['Low'] = Fuzzy.sigmoid((800 - budget) / 100)
            ret['Medium'] = Fuzzy.sigmoid((budget - 700) / 100)
        elif 800 <= budget < 900:
            ret['Low'] = Fuzzy.sigmoid((800 - budget) / 100)
            ret['Medium'] = 1.0
        elif 900 <= budget < 1000:
            ret['Medium'] = 1.0
            ret['High'] = Fuzzy.sigmoid((budget - 1000) / 100)
        elif 1000 <= budget < 1100:
            ret['Medium'] = Fuzzy.sigmoid((1100 - budget) / 100)
            ret['High'] = Fuzzy.sigmoid((budget - 1000) / 100)
        elif 1100 <= budget < 1200:
            ret['Medium'] = Fuzzy.sigmoid((1100 - budget) / 100)
            ret['High'] = 1.0
        elif 1200 <= budget < 1400:
            ret['High'] = 1.0
        elif 1400 <= budget < 1500:
            ret['High'] = 1.0
            ret['Very High'] = Fuzzy.sigmoid((budget - 1500) / 100)
        elif 1500 <= budget < 1600:
            ret['High'] = Fuzzy.sigmoid((1600 - budget) / 100)
            ret['Very High'] = Fuzzy.sigmoid((budget - 1500) / 100)
        elif 1600 <= budget < 1700:
            ret['High'] = Fuzzy.sigmoid((1600 - budget) / 100)
            ret['Very High'] = 1.0
        elif budget >= 1700:
            ret['Very High'] = 1.0

        return ret

    @classmethod
    def fuzzify_over_n(cls, budget: int, guests: int):
        budget /= guests
        CONST: int = 39
        cf: Dict[str, float] = {'Very Low': 0, 'Low': 0, 'Medium': 0, 'High': 0, 'Very High': 0}
        if budget < 300 / CONST:
            cf['Very Low'] = 1.0
        elif 300 / CONST <= budget < 400 / CONST:
            cf['Very Low'] = 1.0
            cf['Low'] = Fuzzy.sigmoid((budget - 400 / CONST) / 100)
        elif 400 / CONST <= budget < 500 / CONST:
            cf['Very Low'] = Fuzzy.sigmoid((500 / CONST - budget) / 100)
            cf['Low'] = Fuzzy.sigmoid((budget - 400 / CONST) / 100)
        elif 500 / CONST <= budget < 600 / CONST:
            cf['Very Low'] = Fuzzy.sigmoid((500 / CONST - budget) / 100)
            cf['Low'] = 1.0
        elif 600 / CONST <= budget < 700 / CONST:
            cf['Low'] = 1.0
            cf['Medium'] = Fuzzy.sigmoid((budget - 700 / CONST) / 100)
        elif 700 / CONST <= budget < 800 / CONST:
            cf['Low'] = Fuzzy.sigmoid((800 / CONST - budget) / 100)
            cf['Medium'] = Fuzzy.sigmoid((budget - 700 / CONST) / 100)
        elif 800 / CONST <= budget < 900 / CONST:
            cf['Low'] = Fuzzy.sigmoid((800 / CONST - budget) / 100)
            cf['Medium'] = 1.0
        elif 900 / CONST <= budget < 1000 / CONST:
            cf['Medium'] = 1.0
            cf['High'] = Fuzzy.sigmoid((budget - 1000) / 100)
        elif 1000 / CONST <= budget < 1100 / CONST:
            cf['Medium'] = Fuzzy.sigmoid((1100 / CONST - budget) / 100)
            cf['High'] = Fuzzy.sigmoid((budget - 1000 / CONST) / 100)
        elif 1100 / CONST <= budget < 1200 / CONST:
            cf['Medium'] = Fuzzy.sigmoid((1100 / CONST - budget) / 100)
            cf['High'] = 1.0
        elif 1200 / CONST <= budget < 1400 / CONST:
            cf['High'] = 1.0
        elif 1400 / CONST <= budget < 1500 / CONST:
            cf['High'] = 1.0
            cf['Very High'] = Fuzzy.sigmoid((budget - 1500 / CONST) / 100)
        elif 1500 / CONST <= budget < 1600 / CONST:
            cf['High'] = Fuzzy.sigmoid((1600 / CONST - budget) / 100)
            cf['Very High'] = Fuzzy.sigmoid((budget - 1500) / 100)
        elif 1600 / CONST <= budget < 1700 / CONST:
            cf['High'] = Fuzzy.sigmoid((1600 / CONST - budget) / 100)
            cf['Very High'] = 1.0
        elif budget >= 1700 / CONST:
            cf['Very High'] = 1.0

        max_val = -1
        max_set = -1
        for key in cf.keys():
            if cf[key] > max_val:
                max_val = cf[key]
                max_set = key

        return max_set
