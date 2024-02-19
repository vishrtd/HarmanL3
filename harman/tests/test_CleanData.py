import os
from unittest import TestCase

from harman.preprocess.CleanData import CleanData
from harman.read.ReadCsv import ReadCsv


class TestCleanData(TestCase):
    def setUp(self) -> None:
        self.file_path = 'dummy_data.csv'
        with open(self.file_path, 'w') as file:
            file.write('datum,M01AB,M01AE\n1/1/2015,1.2,0.00\n1/1/2016,1.3,8.0\n1/1/2017,1.4,3.2\n1/1/2018,1.5,4.2')
        self.csv = ReadCsv(self.file_path)
        self.clean = CleanData(self.csv.data)

    def tearDown(self) -> None:
        os.remove(self.file_path)

    def test_melt_data(self):
        self.assertEquals(self.clean.data.shape, (4, 3))
        id_vars = 'datum'
        value_vars = ['M01AB', 'M01AE']
        self.clean.melt_data(id_vars, value_vars)
        self.assertEquals(self.clean.data.shape, (8, 3))

    def test_get_data(self):
        self.assertIsNotNone(self.clean.get_data())
