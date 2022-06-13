import pandas as pd
import datetime


def format_date(id):
    d, m, y = id.split('/')
    return '{}-{}-{}'.format(y, m, d)

#object containing form256
class Form246:
    def __init__(self, start_date='20220101', end_date='20230101'):
        self.start_date = start_date
        self.end_date = end_date
        
        url = 'https://market.sec.or.th/public/idisc/en/Viewmore/r246-2?ListedType=listed&DateType=1&DateFrom={}&DateTo={}'.format(start_date, end_date)
        table = pd.read_html(url)[0]
        self.table = table

    #list all distinct traders
    def list_trader(self):
        return list(set(self.table['Name of Acquisition/Disposition']))

    #list all distinct tickers
    def list_ticker(self):
        return list(set(self.table['Name of Company']))

    #list all trades by a specific trader
    def filter_trader(self, trader):
        trader_transactions = self.table[self.table['Name of Acquisition/Disposition']==trader]
        trader_transactions['dates'] = trader_transactions['Transaction Date'].map(format_date)  #clean dates
        
        return trader_transactions[['Name of Securities', 'Types', 'dates']].set_index('dates')

    def filter_ticker(self, ticker):
        trader_transactions = self.table[self.table['Name of Securities']==ticker]
        trader_transactions['dates'] = trader_transactions['Transaction Date'].map(format_date)  #clean dates
        
        return trader_transactions[['Name of Acquisition/Disposition', 'Types', 'dates']].set_index('dates')

if __name__ == '__main__':
    #download form246 into object
    form246 = Form246()
    print(test)

'''
           Name of Securities        Types
dates                                     
2022-01-27                 AS  Acquisition
2022-01-06              THREL  Disposition
2022-01-05                 BR  Disposition
2021-12-24                ADD  Acquisition
2021-12-13             NETBAY  Disposition
2021-11-01              BANPU  Disposition
2021-10-29                ADD  Acquisition
2021-10-27                PR9  Disposition
2021-10-19             GRAMMY  Disposition
2021-10-04             NETBAY  Disposition
2021-09-21                 BH  Acquisition
2021-09-09             SAMART  Disposition
2021-08-04                SCN  Disposition
2021-07-20                TSE  Disposition
2021-07-08                 BH  Disposition
2021-06-17               PLAT  Disposition


 00:'Name of Securities'
01:'Name of Acquisition/Disposition'
02:'Types'
03:'Types of Securities'
04:'% Held Before Acquisition/Disposition'
05:'% Held Acquisition/Disposition'
06:'% Held After Acquisition/Disposition'
07:'Transaction Date' ---->>> ['27/01/2022', '06/01/2022', '05/01/2022']
08:'% Group of Held Before Acquisition/Disposition2'
09:'% Group of Held Acquisition/Disposition2'
10:'% Group of Held After Acquisition/Disposition2'
11:'Remark3'
12:'File'
13:'No'
'''