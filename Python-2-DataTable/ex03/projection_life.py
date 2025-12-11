from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


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
    df_inc = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load("life_expectancy_years.csv")
    if df_inc is None or df_life is None:
        return

    if "country" not in df_inc.columns or "country" not in df_life.columns:
        print("Error: CSV file doesn't contain 'country' column.")
        return

    try:
        inc_1900 = df_inc[["country", "1900"]].set_index("country")
        life_1900 = df_life[["country", "1900"]].set_index("country")
    except KeyError as e:
        print(f"Error: {e} not found in data.")
        return

    inc_1900 = inc_1900.map(convert_str_to_float)
    life_1900 = life_1900.map(convert_str_to_float)

    data = pd.merge(inc_1900, life_1900,
                    left_index=True, right_index=True,
                    suffixes=("_income", "_life"))

    plt.scatter(data["1900_income"], data["1900_life"])
    plt.semilogx()
    plt.title("1900")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.show()


if __name__ == "__main__":
    main()
