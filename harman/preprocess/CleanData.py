class CleanData:

    def __init__(self, data):
        """
       Initializes the CleanData object with the provided DataFrame.
       Stores the Pandas DataFrame  in the 'data' attribute.

       :param data (Pandas DataFrame): Pandas DataFrame object.
       """
        self.data = data

    def melt_data(self, id_vars, value_vars):
        """
        UnPivot the dataset on the given variable and columns to be considered as values.
        :param id_vars: (str) Column at which to unpivot the dataset
        :param value_vars: (str or list(str)) Values to take from Column or List of Columns
        :return:
        """
        if type(value_vars) == str:
            # Convert value_vars to list if it is string type
            value_vars = [value_vars]

        self.data = self.data.melt(id_vars=id_vars, value_vars=value_vars)

    def get_data(self):
        """
        Return the DataFrame
        :return: Pandas DataFrame
        """
        return self.data
