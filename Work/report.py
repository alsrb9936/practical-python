# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            temp = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(temp)
            
    return portfolio

def read_prices(filename):
    prices = {}
    
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        
        try:
            for row in rows:
                prices[row[0]] = float(row[1])
        
        except IndexError:
            print('더 이상 참조할 값이 없습니다.')
            
    return prices

portfolio_file = 'Data/portfolio.csv'
prices_file = 'Data/prices.csv'

portfolio = read_portfolio(portfolio_file)
prices = read_prices(prices_file)

Gain = 0

for i in portfolio:
    portfolio_cost = i['price'] 
    now_cost = prices[i['name']]
    shares = i['shares']
    
    Gain += shares * (now_cost - portfolio_cost)
    
print('Gain: ', Gain)
    
