import os
import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''Load a CSV file as a pandas DF, prints its dimensions and returns it.'''
    try:
        if not isinstance(path, str):
            raise AssertionError("Path must be str")
        if not os.path.exists(path):
            raise AssertionError("File doesn't exist")
        ext = os.path.splitext(path)[1].lower()
        if ext != ".csv":
            raise AssertionError("File must be CSV")

        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as e:
        print(f"Error: {e}")
