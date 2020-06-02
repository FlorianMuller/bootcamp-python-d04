# I M P O R T A N T: Execute from parent directory with:
# python -m ex06.MyPlotLib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ex00.FileLoader import FileLoader


class MyPlotLib:
    @staticmethod
    def histogram(df, features):
        fig, axes = plt.subplots(1, len(features))

        for i, feature in enumerate(features):
            axes[i].hist(df[feature].dropna())
            axes[i].set_title(feature)

        plt.show()

    @staticmethod
    def density(df, features):
        for feature in features:
            sns.kdeplot(df[feature])
        plt.show()

    @ staticmethod
    def pair_plot(df, features):
        sns.pairplot(df[features])
        plt.show()

    @ staticmethod
    def box_plot(df, features):
        sns.boxplot(data=df[features])
        plt.show()


if __name__ == "__main__":
    data = FileLoader().load("./data/athlete_events.csv")

    MyPlotLib.histogram(data, ["Height", "Weight"])
    MyPlotLib.density(data, ["Height", "Weight"])
    MyPlotLib.pair_plot(data, ["Weight", "Height"])
    MyPlotLib.box_plot(data, ["Weight", "Height"])
