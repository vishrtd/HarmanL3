import os
from unittest import TestCase

from harman.preprocess.CreateFeatures import CreateFeatures
from harman.read.ReadCsv import ReadCsv


class TestCreateFeatures(TestCase):

    def setUp(self) -> None:
        self.file_path = 'dummy_data.csv'
        with open(self.file_path, 'w') as file:
            file.write('datum,variable,value\n1/1/2015,M01AB,0.00\n1/1/2016,M01AE,8.0\n1/1/2017,M01AB,3.2\n1/1/2018,M01AE,4.2')
        self.csv = ReadCsv(self.file_path)
        self.features = CreateFeatures(self.csv.data)

    def tearDown(self) -> None:
        os.remove(self.file_path)

    def test_calculate_rolling_average(self):
        self.assertTrue('value_1' not in self.features.data.columns)
        self.assertTrue('value_2' not in self.features.data.columns)
        self.features.calculate_rolling_average(1, 2)
        self.assertTrue('value_1' in self.features.data.columns)
        self.assertTrue('value_2' in self.features.data.columns)
        self.assertEquals(round(self.features.data['value_1'].sum(), 1), 15.4)
        self.assertEquals(round(self.features.data['value_2'].sum(), 1), 13.3)
        # print(self.features.get_data().sum())

    def test_get_data(self):
        self.assertIsNotNone(self.features.get_data())
