import matplotlib.pyplot as plt
from form246 import Form246
from stock import get_quote
from tqdm import tqdm

active_form246 = Form246(start_date='20220101', end_date='20990101') #list active traders
form246 = Form246(start_date='20180101', end_date='20990101') #long full history

active_traders = active_form246.list_trader()

for trader in active_traders: #active_form246.list_trader():
    transactions = form246.trader_transaction(trader)
    for date, ticker, type in tqdm(transactions.to_records()):
        try:
            transaction = get_quote(ticker, date, 60)
            if type == 'Acquisition':
                transaction.plot(label=ticker, color='green')
            else: #Disposition
                transaction.plot(label=ticker, color='red')
        except:
            pass
    plt.title(trader)
    plt.xlabel('days')
    plt.legend()
    plt.savefig('plot/{}.jpeg'.format(trader))
    plt.clf()

'''
    stock = Stock(start_date='20200101', end_date='20990101')
    #form246 -> get transaction date of Purchase/Sale [ticker, transaction type, transaction date]
    transactions_df = form246.trader_transaction(trader)
    date_df = transactions_df['Transaction Date']


    #Stock -> each pull from Stock
    quote = Stock(ticker).quote()


    #plot

    #save plot




def format_date(id):
    d, m, y = id.split('/')
    return '{}-{}-{}'.format(y, m, d)


#import form59
insider_volume = pd.read_csv('data/form59.csv')
#list tickers
table = pd.read_csv('data/form59.csv')
tickers = list(set(list(table['Name of Company'])))

#screen tickers
#screened_tickers = form59_screener.screen_insider_buy(tickers, 30, 10000000)
#print(screened_tickers)

#save figures
#form59_screener.form59_plotter(screened_tickers, save=True, show=False)

#show individual figure
form59_screener.form59_plotter(['GUNKUL'], save=False, show=True)
'''