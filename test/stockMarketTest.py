#!/usr/bin/env python3

"""From the root directory of this repository, execute tests and check results
with:

python3 -m unittest test.stockMarketTest
"""

import unittest
import math
import stockMarket
import time

class TeststockMarket(unittest.TestCase):

    def testCanCalculateDividendYieldForStock(self):
        stock= stockMarket.Stock('test/data.csv')
        self.assertAlmostEqual(0, stock.get_dividend_yield(stock= 'TEA', ticker_price= 2))
        self.assertAlmostEqual(2.667, stock.get_dividend_yield(stock= 'POP', ticker_price= 3), places= 3)
        self.assertAlmostEqual(0.667, stock.get_dividend_yield(stock= 'GIN', ticker_price= 3), places= 3)

        self.assertRaises(stockMarket.StockException, stock.get_dividend_yield, stock= 'FOOBAR', ticker_price= 3)

    def testCanCalculatePERatioForStock(self):
        stock= stockMarket.Stock('test/data.csv')
        self.assertTrue(math.isnan(stock.get_pe_ratio(stock= 'TEA', ticker_price= 2)))
        self.assertAlmostEqual(3/2.667, stock.get_pe_ratio(stock= 'POP', ticker_price= 3), places= 3)

    def testCanRecordTrade(self):
        stock= stockMarket.Stock('test/data.csv')
        stock.record_trade(stock= 'POP', quantity= 10, sold= True, price= 5)
        self.assertEqual(1, len(stock.trade))

        stock.record_trade(stock= 'TEA', quantity= 10, sold= True, price= 5)
        self.assertEqual(2, len(stock.trade))

        self.assertRaises(stockMarket.StockException, stock.record_trade, stock= 'FOOBAR', quantity= 10, sold= True, price= 5)

    def testCanCalculateStockPrice(self):
        
        stock= stockMarket.Stock('test/data.csv')

        self.assertTrue(math.isnan(stock.get_stock_price('POP')))
        
        stock.record_trade(stock= 'POP', quantity= 10, sold= True, price= 5)
        stock.record_trade(stock= 'POP', quantity= 15, sold= True, price= 4)

        self.assertTrue(math.isnan(stock.get_stock_price('TEA')))

        stock.record_trade(stock= 'TEA', quantity= 100, sold= True, price= 50)
        stock.record_trade(stock= 'TEA', quantity= 150, sold= True, price= 40)

        self.assertAlmostEqual(4.4, stock.get_stock_price('POP'))
        self.assertAlmostEqual(44.0, stock.get_stock_price('TEA'))
        
        time.sleep(2)
        self.assertTrue(math.isnan(stock.get_stock_price('TEA', last_minutes= 0.01)))

    def testCanGetAllShareIndex(self):
        stock= stockMarket.Stock('test/data.csv')

        self.assertTrue(math.isnan(stock.get_all_share_index()))

        stock.record_trade(stock= 'POP', quantity= 10, sold= True, price= 1)
        stock.record_trade(stock= 'POP', quantity= 15, sold= True, price= 2)
        stock.record_trade(stock= 'TEA', quantity= 100, sold= True, price= 3)
        stock.record_trade(stock= 'TEA', quantity= 150, sold= True, price= 4)
        
        self.assertAlmostEqual(2.21, stock.get_all_share_index(), places= 2)

if __name__ == '__main__':
    unittest.main()