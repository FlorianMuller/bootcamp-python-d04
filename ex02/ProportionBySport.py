# I M P O R T A N T: Execute from parent directory with:
# python -m ex02.ProportionBySport
import pandas as pd
from ex00.FileLoader import FileLoader


def proportionBySport(df, year, sport, gender):
    all_data = df.loc[
        (df["Sex"] == gender) &
        (df["Year"] == year)
    ].drop_duplicates(subset="Name")

    all_player = all_data.shape[0]
    sport_player = all_data.loc[all_data["Sport"] == sport].shape[0]

    return sport_player / all_player * 100


if __name__ == "__main__":
    data = FileLoader().load("./data/athlete_events.csv")

    print(proportionBySport(data, 2004, 'Tennis', 'F'))
