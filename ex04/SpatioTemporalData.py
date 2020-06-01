# I M P O R T A N T: Execute from parent directory with:
# python -m ex04.SpatioTemporalData
import pandas as pd
from dataclasses import dataclass
from ex00.FileLoader import FileLoader


@dataclass
class SpatioTemporalData:
    df: pd.DataFrame

    def when(this, location):
        return this.df.loc[this.df["City"] == location]["Year"].unique()

    def where(this, date):
        return this.df.loc[this.df["Year"] == date]["City"].unique()


if __name__ == "__main__":
    data = FileLoader().load("./data/athlete_events.csv")

    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
