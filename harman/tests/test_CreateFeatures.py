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
        self.features.calculate_rolling_average(1, 2)
        self.assertTrue('value_1' in self.features.data.columns)
        self.assertTrue('value_2' in self.features.data.columns)

    def test_get_data(self):
        self.assertIsNotNone(self.features.get_data())
