import unittest

from harman.tests import test_CleanData, test_CreateFeatures, test_ReadCsv

clean_data_suite = unittest.TestLoader().loadTestsFromTestCase(test_CleanData.TestCleanData)
create_feature_suite = unittest.TestLoader().loadTestsFromTestCase(test_CreateFeatures.TestCreateFeatures)
read_csv_suite = unittest.TestLoader().loadTestsFromTestCase(test_ReadCsv.TestReadCsv)

test_suites = [clean_data_suite, create_feature_suite, read_csv_suite]
master_suite = unittest.TestSuite(test_suites)

if __name__ == '__main__':

    unittest.TextTestRunner().run(master_suite)
