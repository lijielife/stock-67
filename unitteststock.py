#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from stock import Stock, StockException

class TestStock(unittest.TestCase):
    """
    Contains set of unittests for Stock class
    """
    def setUp(self):
        self.validfile = 'sample_data.csv'
        self.non_existing_file = 'invalid.csv'

    def tearDown(self):
        pass

    def test_success(self):
        """
	Check for success scenario where highest stock price is returned correctly
        """
        s = Stock(self.validfile)
        s.read_stock_data()
        company = s.csv_data[0][2:][0]
	csv_sorted = s.sort_stocks_by_company(company, True)
	self.assertTrue(s.print_highest_price(csv_sorted[1:2],company,2))

    def test_read_stock_data(self):
        """
        Check if the csv data is loaded and parsed correctly
        """
        s = Stock(self.validfile)
        self.assertTrue(s.read_stock_data())

    def test_with_non_existing_file(self):
        """
        Check if StockException is raised for non_existing_file_input
        """
        s = Stock(self.non_existing_file)
        self.assertRaises(StockException, s.read_stock_data)

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestStock)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
    exit()
