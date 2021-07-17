'''
This is the module which contains unit testing of two functions for sample.
'''
#---------------------------------------------------------------------------------------
'''
Unit test library is imported to perform unit testing.
'''
#---------------------------------------------------------------------------------------
import unittest
import CLI_Version as CLI_V
import warnings
warnings.simplefilter(action="ignore", category=ResourceWarning)

#creating a class for unit test.
class TestData_ReaderValue(unittest.TestCase):
    def test_length(self):
        #to check length of the dataframe
        data_length_check = CLI_V.data_check_unittest('AAPL', '2020-08-01', '2020-08-30')
        self.assertEqual(len(data_length_check),21)
    def test_last(self):
        #to check the last date value of the dataframe
        data_lastelement = CLI_V.data_check_last('AAPL','2020-08-01','2020-08-30')
        self.assertEqual(str(data_lastelement.index[-1]),'2020-08-28 00:00:00')

if __name__ == '__main__':
    unittest.main()



