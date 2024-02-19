class CreateFeatures:
    def __init__(self, data):
        """
       Initializes the CreateFeatures object with the provided DataFrame.
       Stores  the Pandas DataFrame  in the 'data' attribute.

       :param data (Pandas DataFrame): Pandas DataFrame object.
       """
        self.data = data
        self.num_days = []

    def calculate_rolling_average(self, *num_days):
        """
        Calculate the rolling average for all numeric columns.
        :param num_days: (int) Number of days.
        :return: None
        """
        self.num_days = num_days
        for col in self.data.columns:
            for days in num_days:
                if self.data[col].dtype == float or self.data[col].dtype == int:
                    self.data[f'{col}_{days}'] = self.data[col].rolling(window=days).mean()
                    self.data[f'{col}_{days}'] = self.data[f'{col}_{days}'].shift(-1*days)

    def get_data(self):
        """
        Return the DataFrame
        :return: Pandas DataFrame
        """
        return self.data
