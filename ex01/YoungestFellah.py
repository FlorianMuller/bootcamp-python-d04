# I M P O R T A N T: Execute from parent directory with:
# python -m ex01.YoungestFellah
import pandas as pd
from ex00.FileLoader import FileLoader


def youngestFellah(df, year):
    return {
        "f": df.loc[(df["Year"] == year) & (df["Sex"] == "F")]["Age"].min(),
        "m": df.loc[(df["Year"] == year) & (df["Sex"] == "M")]["Age"].min()
    }


if __name__ == "__main__":
    data = FileLoader().load("./data/athlete_events.csv")

    print("1896", youngestFellah(data, 1896))
    print("2004", youngestFellah(data, 2004))
    print("2016", youngestFellah(data, 2016))

    pass
