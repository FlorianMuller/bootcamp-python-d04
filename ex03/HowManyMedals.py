# I M P O R T A N T: Execute from parent directory with:
# python -m ex03.HowManyMedals
import pandas as pd
from ex00.FileLoader import FileLoader


def howManyMedals(df, name):
    player_data = df.loc[df["Name"] == name]

    medals = {}
    for year in player_data["Year"].unique():
        year_count = player_data.loc[
            player_data["Year"] == year
        ]["Medal"].value_counts()

        medals[year] = {
            "G": year_count["Gold"] if "Gold" in year_count else 0,
            "S": year_count["Silver"] if "Silver" in year_count else 0,
            "B": year_count["Bronze"] if "Bronze" in year_count else 0
        }

    return medals


if __name__ == "__main__":
    data = FileLoader().load("./data/athlete_events.csv")

    print(howManyMedals(data, 'Kjetil Andr Aamodt'))
