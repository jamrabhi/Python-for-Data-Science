import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''Returns a truncated version of the array and its shape.'''
    try:
        if not isinstance(family, list):
            raise AssertionError("Family must be a list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("start and end must be int")
        if not all(isinstance(row, list) for row in family):
            raise AssertionError("Family must be a 2D list")
        if len(family) > 0:
            row_length = len(family[0])
            if not all(len(row) == row_length for row in family):
                raise AssertionError("All rows must have same size")

        np_family = np.array(family)
        print(f"My shape is : {np_family.shape}")

        family_sliced = np_family[start:end]
        print(f"My new shape is : {family_sliced.shape}")

        return family_sliced.tolist()

    except AssertionError as err:
        print(f"AssertionError: {err}")
        return []
