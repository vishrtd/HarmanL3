import pandas as pd


class ReadCsv:

    def __init__(self, file_path):
        """
        Initializes the ReadCsv object with the provided CSV file path.
        Reads the CSV file into a Pandas DataFrame and stores it in the 'data' attribute.

        :param file_path (str): The path to the CSV file.
        """
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

    def parse_date_column(self, column_name):
        """
        Parse the specified column in the DataFrame as datetime.

        :param column_name: (str) The name of the column to parse.
        :return: None
        """
        self.data[column_name] = pd.to_datetime(self.data[column_name])

    def drop_columns(self, *cols):
        """
        Drop the specified column or columns from the DataFrame.
        :param cols: (List) List of columns to drop from the DataFrame
        :return: None
        """

        self.data.drop(*cols, axis=1, inplace=True)

    def get_data(self):
        """
        Return the DataFrame
        :return: Pandas DataFrame
        """
        return self.data
