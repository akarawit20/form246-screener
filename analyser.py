import datetime
import pandas as pd

def calculate_table(table):
    #calculate buy and sell column

    #date
    table['Transaction Date'] = pd.to_datetime(table['Transaction Date'], format='%d/%m/%Y')
    table.set_index('Transaction Date', inplace=True)

    #buy
    buy_table = table[table['The methods of Acquisition/Disposition']=='Buy']
    purchase_table = table[table['The methods of Acquisition/Disposition']=='Purchase']
    buy_table = buy_table.append(purchase_table)
    buy_table.sort_index(inplace=True)
    buy_value_series = buy_table['Average Price (baht)']*buy_table['Amount']
    buy_value_series = buy_value_series.groupby(level=0).sum()

    #sell
    sell_table = table[table['The methods of Acquisition/Disposition']=='Sell']
    sale_table = table[table['The methods of Acquisition/Disposition']=='Sale']
    sell_table = sell_table.append(sale_table)
    sell_table.sort_index(inplace=True)
    sell_value_series = sell_table['Average Price (baht)']*sell_table['Amount']
    sell_value_series = sell_value_series.groupby(level=0).sum()
    
    return [buy_value_series, sell_value_series]

def high_insider_buy(table, day_passed, threshold):
    #create start_date_str
    today = datetime.date.today()
    start_date =  today - datetime.timedelta(days=day_passed)
    start_date_str = start_date.strftime('%Y-%m-%d')

    date_bought,date_sold = calculate_table(table)
    date_bought = date_bought.reset_index()
    date_bought = date_bought[date_bought['Transaction Date']>start_date_str]

    return date_bought[0].sum() > threshold


if __name__ == '__main__':
    #import form59
    insider_volume = pd.read_csv('data/form59.csv')

    #list tickers
    tickers = pd.read_csv('tickers.csv', sep=', ', header=None)
    tickers = tickers.values[0]

    tickers = ['TTA', 'PTT']
    for ticker in tickers:
        ticker_form59 = insider_volume[insider_volume['Name of Company'] == ticker]
        h = high_insider_buy(ticker_form59, 30, 1000000)
        print(h)
