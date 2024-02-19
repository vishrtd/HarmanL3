class CleanData:

    def __init__(self, data):
        self.data = data

    def melt_data(self, id_vars, value_vars):
        if type(value_vars) == str:
            value_vars = [value_vars]

        self.data = self.data.melt(id_vars=id_vars, value_vars=value_vars)

    def get_data(self):
        return self.data
