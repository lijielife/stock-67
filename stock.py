#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os.path
import csv
import operator
import unittest

class StockException(Exception):
    """
    Generic Stock Exception Class
    """
    pass

class Stock(object):
    """
    It loads stock price data from csv file for multiple companies for specific period.
    Methods are defined to get highest stock price for all companies
    """
    def __init__(self,input_file):
        self.input_file = input_file
        self.csv_data = None

    def read_stock_data(self, delimiter=','):
        """
        It loads, parses and stores stock price data from csv file
        """
        if not os.path.isfile(self.input_file):
            raise StockException ("%s does not exist!" % self.input_file)
	    exit()

        with open(self.input_file, 'rb') as csv_file:
            stock_reader = csv.reader(csv_file, delimiter=delimiter)
            csv_content = list(stock_reader)
            for record in csv_content[1:]:
                for i,r in enumerate(record):
                    try:
                        record[i] = int(r)
                    except ValueError:
                        pass
            self.csv_data = csv_content
        return True

    def sort_stocks_by_company(self, col, reverse=False):
        """
        Sorts stored stock prices data for each company
        """
        header = self.csv_data[0]
        content = self.csv_data[1:]
        if isinstance(col, str):
            col_index = header.index(col)
        else:
            col_index = col
        content = sorted(content,
                  key=operator.itemgetter(col_index),
                  reverse=reverse)
        content.insert(0, header)
        return content

    def print_highest_price(self,stock_records,company,company_index):
        print "\nHighest share price for '%s':" % company
        print '{:>10} {:>10} {:>15}'.format('Year','Month','StockPrice')
        for row in stock_records:
            row = [str(e) for e in row]
            print '{:>10} {:>10} {:>15}'.format(row[0],row[1],row[company_index])
        return True

if __name__ == '__main__':
    from unitteststock import TestStock
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-i',dest="input_file",action='store',help="Input data for processing")
        parser.add_argument('-t',action='store_true',help="Test the code")
    except argparse.ArgumentParser as e:
        print e

    args = parser.parse_args()
    if not any(vars(args).values()):
        parser.print_help()

    if args.input_file:
        print "Processing input_file:",args.input_file
        s = Stock(args.input_file)
	s.read_stock_data()
        companies = s.csv_data[0][2:]
        for company in companies:
            csv_sorted = s.sort_stocks_by_company(company, True)
            s.print_highest_price(csv_sorted[1:2],company,s.csv_data[0].index(company))

    if args.t:
        print "\nTest in progress:"
        test_suite = unittest.TestLoader().loadTestsFromTestCase(TestStock)
        unittest.TextTestRunner(verbosity=2).run(test_suite)
        exit()
