import analyser

from tqdm import tqdm
import pandas as pd
import matplotlib.dates as mdates
from matplotlib import pyplot as plt
from matplotlib.widgets import MultiCursor

#import form59
insider_volume = pd.read_csv('data/form59.csv')

#list tickers
tickers = list(set(list(insider_volume['Name of Company'])))

#tqdm(files)
def form59_plotter(tickers, save=True, show=False):
    for ticker in tqdm(tickers):

        #get price
        ticker_price = pd.read_csv('data/stock_quotes/{}.csv'.format(ticker))
        ticker_price['Date'] = pd.to_datetime(ticker_price['Date'])
        ticker_price = ticker_price.set_index('Date')
        
        #get insider value
        ticker_form59 = insider_volume[insider_volume['Name of Company'] == ticker]
        buy_value, sell_value = analyser.calculate_table(ticker_form59)


        fig, ax = plt.subplots(3, sharex=True)
        fig.suptitle(ticker)

        #ticker_price.plot(ax=axes[0], kind='line', title=ticker, color='b', grid=True)
        #buy_value.plot(ax=axes[1], kind='bar', color='g', grid=False)
        #sell_value.plot(ax=axes[1], kind='bar', color='r', grid=False)

        ax[0].plot(ticker_price.index, ticker_price.values)
        ax[1].scatter(buy_value.index, buy_value.values, color='g')
        ax[2].scatter(sell_value.index, sell_value.values, color='r')

        ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        
        ax[1].set_yscale('log')
        ax[1].set_ylim([10**3, 10**9])
        ax[2].set_yscale('log')
        ax[2].set_ylim([10**3, 10**9])

        multi = MultiCursor(fig.canvas, (ax[0], ax[1], ax[2]), color='r', lw=1)
        if show:
            plt.show()
            
        if save:
            #fig.tight_layout()# otherwise the right y-label is slightly clipped
            plt.savefig('figures/{}'.format(ticker))

def screen_insider_buy(tickers, day_passed, bought_value):
    #screen for ticker with high recent insider buy
    screened_tickers = []
    for ticker in tqdm(tickers):
        ticker_form59 = insider_volume[insider_volume['Name of Company'] == ticker]
        high_insider_buy = analyser.high_insider_buy(ticker_form59, day_passed, bought_value)
        if high_insider_buy:
            screened_tickers.append(ticker)
    return screened_tickers



