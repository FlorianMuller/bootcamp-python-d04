# I M P O R T A N T: Execute from parent directory with:
# python -m ex05.HowManyMedalsByCountry
import pandas as pd
from ex00.FileLoader import FileLoader


def howManyMedalsByCountry(df, team):
    team_data = df.loc[
        df['Team'] == team
    ].drop_duplicates(subset=["Year", "Event", "Medal"])

    medals = {}
    for year in team_data["Year"].unique():
        year_count = team_data.loc[
            team_data["Year"] == year
        ]["Medal"].value_counts()

        medals[year] = {
            "G": year_count["Gold"] if "Gold" in year_count else 0,
            "S": year_count["Silver"] if "Silver" in year_count else 0,
            "B": year_count["Bronze"] if "Bronze" in year_count else 0
        }

    return medals


if __name__ == "__main__":
    data = FileLoader().load("./data/athlete_events.csv")

    res = howManyMedalsByCountry(data, "France")

    for year in sorted(res.keys()):
        print(f"{year} -> {res[year]}")
