import datetime
import yfinance as yf

def get_quote(ticker, date, length):
    start_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    end_date = start_date + datetime.timedelta(days=length)

    stock_df = yf.download('{}.BK'.format(ticker), start_date, end_date)        
    
    start_price = stock_df['Adj Close'][0]
    normalized_price = stock_df['Adj Close'].reset_index(drop=True)/start_price
    return normalized_price

if __name__ == '__main__':
    print(get_quote('PTT', '2021-01-01', 30))
'''
Date
2021-01-04    1.000000
2021-01-05    0.988235
2021-01-06    1.005882
2021-01-07    1.000000
2021-01-08    1.005882
2021-01-11    1.011765
2021-01-12    1.029412
2021-01-13    1.047059
2021-01-14    1.035294
2021-01-15    1.017647
2021-01-18    1.000000
2021-01-19    0.964706
2021-01-20    0.964706
2021-01-21    0.958823
2021-01-22    0.929412
2021-01-25    0.941176
2021-01-26    0.935294
2021-01-27    0.923529
2021-01-28    0.905882
2021-01-29    0.888235
Name: Adj Close, dtype: float64
'''