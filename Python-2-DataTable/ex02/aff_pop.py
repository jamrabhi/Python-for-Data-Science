'''Loads population_total.csv, and displays France population vs Belgium.'''
from load_csv import load
import matplotlib.pyplot as plt


def convert_str_to_float(value: str) -> float:
    '''Convert population strings with K, M, B suffixes to float.'''
    if not isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return float(0.0)

    suffix = value[-1].upper()
    number = value[:-1]

    try:
        if suffix == 'K':
            return float(number) * 1_000
        elif suffix == 'M':
            return float(number) * 1_000_000
        elif suffix == 'B':
            return float(number) * 1_000_000_000
        else:
            return float(value)
    except ValueError:
        return float(0.0)


def main():
    df = load("population_total.csv")
    if df is None:
        return

    if "country" not in df.columns:
        print("Error: CSV file doesn't contain 'country' column.")
        return

    df.set_index("country", inplace=True)
    try:
        FR = df.loc["France"][:"2050"].apply(convert_str_to_float)
        BE = df.loc["Belgium"][:"2050"].apply(convert_str_to_float)
    except KeyError as e:
        print(f"Error: {e} not found in data.")
        return

    plt.plot(FR.index.astype(int), FR.values, label="France")
    plt.plot(BE.index.astype(int), BE.values, label="Belgium")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.legend(loc="lower right")

    # Customize x ticks
    plt.xticks(FR.index.astype(int)[::40])

    # Customize y ticks
    max_val = max(FR.max(), BE.max())
    ticks = list(range(0, int(max_val), 20_000_000))
    labels = [f"{t//1_000_000}M" if t != 0 else "0" for t in ticks]
    plt.yticks(ticks, labels)

    plt.show()


if __name__ == "__main__":
    main()
