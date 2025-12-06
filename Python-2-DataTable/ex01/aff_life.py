'''Loads life_expectancy_years.csv, and displays France life expectancy.'''
from load_csv import load
import matplotlib.pyplot as plt


def main():
    df = load("life_expectancy_years.csv")
    if df is None:
        return

    if "country" not in df.columns:
        print("Error : File doesn't contain 'country' column.")
        return

    french = df[df["country"] == "France"]
    if french.empty:
        print("Error: No data")
        return

    years = french.columns[1:].astype(int)
    ages = french.iloc[0, 1:].astype(float)

    plt.plot(years, ages)
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("France Life expectancy Projections")
    plt.show()


if __name__ == "__main__":
    main()
