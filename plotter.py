import matplotlib.pyplot as plt
import numpy as np

def plotter(line, weight, label):
    # importing package

    # create data
    #x = [[1,2,3,4,5], [3,3,3,3,3]]

    plt.plot(line, linestyle="-", color='blue', alpha=weight)

    plt.title(label)
    plt.show()




'''
class Plotter:
    def __init__(self, indider_value, quote):
        self.ticker_price = quote
        self.buy_value, self.sell_value = analyser.calculate_table(indider_value)

    def save_plot(self, ticker):
        fig, ax = plt.subplots(3, sharex=True)
        fig.suptitle(ticker)

        #ticker_price.plot(ax=axes[0], kind='line', title=ticker, color='b', grid=True)
        #buy_value.plot(ax=axes[1], kind='bar', color='g', grid=False)
        #sell_value.plot(ax=axes[1], kind='bar', color='r', grid=False)

        ax[0].plot(self.ticker_price.index, self.ticker_price.values)
        ax[1].scatter(self.buy_value.index, self.buy_value.values, color='g')
        ax[2].scatter(self.sell_value.index, self.sell_value.values, color='r')

        ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        
        ax[1].set_yscale('log')
        ax[1].set_ylim([10**3, 10**9])
        ax[2].set_yscale('log')
        ax[2].set_ylim([10**3, 10**9])

        multi = MultiCursor(fig.canvas, (ax[0], ax[1], ax[2]), color='r', lw=1)
            
        #fig.tight_layout()# otherwise the right y-label is slightly clipped
        plt.savefig('figures/{}'.format(ticker))




#import form59
insider_volume = pd.read_csv('data/form59.csv')

#list tickers
tickers = list(set(list(insider_volume['Name of Company'])))

#tqdm(files)


def screen_insider_buy(tickers, day_passed, bought_value):
    #screen for ticker with high recent insider buy
    screened_tickers = []
    for ticker in tqdm(tickers):
        ticker_form59 = insider_volume[insider_volume['Name of Company'] == ticker]
        high_insider_buy = analyser.high_insider_buy(ticker_form59, day_passed, bought_value)
        if high_insider_buy:
            screened_tickers.append(ticker)
    return screened_tickers

'''

