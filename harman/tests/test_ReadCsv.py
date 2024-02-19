import os
from unittest import TestCase

import numpy

from harman.read.ReadCsv import ReadCsv


class TestReadCsv(TestCase):

    def setUp(self) -> None:
        self.file_path = 'dummy_data.csv'
        with open(self.file_path, 'w') as file:
            file.write('datum,variable,value\n1/1/2015,M01AB,0.00\n1/1/2016,M01AE,8.0\n1/1/2017,M01AB,3.2\n1/1/2018,M01AE,4.2')
        self.read_csv = ReadCsv(self.file_path)

    def tearDown(self) -> None:
        os.remove(self.file_path)

    def test_read_csv(self):
        self.assertIsNotNone(self.read_csv.data)

    def test_parse_date_column(self):
        self.assertIsInstance(self.read_csv.data['datum'], object)
        self.read_csv.parse_date_column('datum')
        # TODO Check dtype matches datetime64
        # self.assertNotIsInstance(self.read_csv.data['datum'], object)
        # self.assertIsInstance(self.read_csv.data['datum'], numpy.dtype.type['datetime64'])
        # self.assertIsInstance(self.read_csv.data['datum'], 'O')
