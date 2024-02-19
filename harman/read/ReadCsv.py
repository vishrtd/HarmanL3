import pandas as pd


class ReadCsv:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

    def parse_date_column(self, column_name):
        self.data[column_name] = pd.to_datetime(self.data[column_name])

    def drop_columns(self, *cols):
        self.data.drop(*cols, axis=1, inplace=True)

    def get_data(self):
        return self.data



