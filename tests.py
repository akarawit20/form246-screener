import form59_screener
import pandas as pd

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
