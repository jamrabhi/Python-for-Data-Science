import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    '''Calculate BMI for given heights and weights.'''
    try:
        if len(height) != len(weight):
            raise AssertionError("Height and weight must have the same length")
        if len(height) == 0 or len(weight) == 0:
            raise AssertionError("Height and weight lists cannot be empty")
        if not all(isinstance(h, (int, float)) and h > 0 for h in height):
            raise AssertionError("All heights must be positive numbers")
        if not all(isinstance(w, (int, float)) and w > 0 for w in weight):
            raise AssertionError("All weights must be positive numbers")

        height_array = np.array(height)
        weight_array = np.array(weight)
        bmi = weight_array / np.square(height_array)
        return bmi.tolist()

    except AssertionError as err:
        print(f"AssertionError: {err}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''Return a list indicating if each BMI exceeds the given limit.'''
    try:
        if not (isinstance(limit, int) and limit > 0):
            raise AssertionError("Limit must be > 0")
        if not isinstance(bmi, list):
            raise AssertionError("bmi must be a list")
        if not all(isinstance(b, (int, float)) and b > 0 for b in bmi):
            raise AssertionError("bmi must contain only int/float and > 0")

        result = np.array(bmi) > limit
        return result.tolist()

    except AssertionError as err:
        print(f"AssertionError: {err}")
        return []
