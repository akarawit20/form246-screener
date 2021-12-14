from tqdm import tqdm
import pandas as pd
import yfinance as yf
from yfinance import ticker

def get_form59(start_date, end_date, path):
    
    url = 'https://market.sec.or.th/public/idisc/en/Viewmore/r59-2?DateType=1&DateFrom={}&DateTo={}'.format(start_date, end_date)
    #import table from web
    table = pd.read_html(url)[0]

    #clean table
    table = table[~table['Amount'].str.contains('Revoked by Reporter')] #remove revoked order
    table = table[~table['Average Price (baht)'].str.contains('-')] #remove transfer order
    table = table.drop(columns=['Remark'])
    table = table[table['The methods of Acquisition/Disposition'] != 'Acceptance of Transfer']
    table = table[table['The methods of Acquisition/Disposition'] != 'Transfer']
    #table['Value'] = table['Amount'].astype(int) * table['Average Price (baht)'].astype(float)

    #name to ticker
    name_to_ticker = lambda name: name[(len(name)-name[::-1].index('(')):-1]

    #raplece name with ticker
    ticker_series = table['Name of Company'].map(name_to_ticker)
    table['Name of Company'] = ticker_series
    #save table
    table.to_csv(path, index=False)

def get_price(ticker, start, end):

    stock_df = yf.download('{}.BK'.format(ticker), start, end)
    stock_df.head()

    return stock_df['Adj Close']

if __name__ == '__main__':
    #year/month/date
    start_date = '2018-01-01'
    end_date = '2021-12-31'

    #scrape form59
    #get_form59(start_date.replace('-', ''), end_date.replace('-', ''), 'data/form59.csv')

    #scrape stocks
    table = pd.read_csv('data/form59.csv')
    tickers = list(set(list(table['Name of Company'])))
    tickers.sort()
    for ticker in tqdm(tickers[360:]):
        price = get_price(ticker, start_date, end_date)
        price.to_csv('data/stock_quotes/{}.csv'.format(ticker))


