import pandas as pd


class FileLoader:
    @staticmethod
    def load(path):
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
        return df

    @staticmethod
    def display(df, n):
        print(df[:n])


if __name__ == "__main__":
    # test the FileLoader class
    loader = FileLoader()
    data = loader.load("../data/athlete_events.csv")
    loader.display(data, 12)
