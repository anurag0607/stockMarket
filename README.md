The code for the *Super Simple Stock* exercise is in `stockMarket.py`.
Tests and test data are in `test/stockMarketTest.py` and `test/data.csv`
respectively.

# Dependencies

* Python 3.x

* Additional modules not in the standard library can be installed with:

```
pip3 install -r requirements.txt
```

# Usage example

```
import stockMarket

stock= stockMarket.Stock('test/data.csv')

stock.get_dividend_yield(stock= 'POP', ticker_price= 3)

stock.get_pe_ratio(stock= 'POP', ticker_price= 3)

stock.record_trade(stock= 'POP', quantity= 10, sold= True, price= 5)
stock.record_trade(stock= 'POP', quantity= 11, sold= True, price= 6)
stock.record_trade(stock= 'POP', quantity= 12, sold= True, price= 7)
print(stock.trade)

stock.get_stock_price('POP')

stock.get_all_share_index()
```

# Run tests

```
python3 -m unittest test.stockMarketTest
```

----

Author: Anurag Verma