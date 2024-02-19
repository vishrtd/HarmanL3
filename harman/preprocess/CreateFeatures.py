class CreateFeatures:
    def __init__(self, data):
        self.data = data
        self.num_days = []

    def calculate_rolling_average(self, *num_days):
        self.num_days = num_days
        for col in self.data.columns:
            for days in num_days:
                if self.data[col].dtype == float or self.data[col].dtype == int:
                    self.data[f'{col}_{days}'] = self.data[col].rolling(window=days).mean()

    def get_data(self):
        return self.data
