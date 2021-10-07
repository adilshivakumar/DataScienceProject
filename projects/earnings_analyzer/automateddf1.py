from datetime import date, timedelta

import dateutil.parser
import pandas as pd
import pandas_market_calendars as mcal
import yahoo_fin.stock_info as si
from pandas.tseries.holiday import (AbstractHolidayCalendar, GoodFriday,
                                    Holiday, USLaborDay, USMartinLutherKingJr,
                                    USMemorialDay, USPresidentsDay,
                                    USThanksgivingDay, nearest_workday)
from pandas.tseries.offsets import CustomBusinessDay
from pandas_datareader import data as web
from yahoo_earnings_calendar import YahooEarningsCalendar

start = date(2008, 3, 11)
start_date = pd.to_datetime(start)
end = date(2021, 7, 29)
end_date = pd.to_datetime(end)


TICKER = 'AAPL'
aapl_earnings_hist = si.get_earnings_history(TICKER)
frame = pd.DataFrame.from_dict(aapl_earnings_hist)
frame['startdatetime'] = pd.to_datetime(frame['startdatetime'])
frame['startdatetime'] = frame['startdatetime'].dt.date

frame_filtered = frame[frame['startdatetime'] >= start]
frame_filtered = frame_filtered[frame_filtered['startdatetime'] <= end]
earnings_date_final = frame_filtered.drop(['ticker','companyshortname','startdatetimetype','epsestimate','epsactual','epssurprisepct','timeZoneShortName','gmtOffsetMilliSeconds','quoteType'], axis = 1)

print(earnings_date_final)
  
print(earnings_date_final.shape)
class USTradingCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('NewYearsDay', month=1, day=1, observance=nearest_workday),
        USMartinLutherKingJr,
        USPresidentsDay,
        GoodFriday,
        USMemorialDay,
        Holiday('USIndependenceDay', month=7, day=4, observance=nearest_workday),
        USLaborDay,
        USThanksgivingDay,
        Holiday('Christmas', month=12, day=25, observance=nearest_workday)
    ]
US_BUSINESS_DAY = CustomBusinessDay(calendar=USTradingCalendar())
frames = []
for index, e_d in earnings_date_final.iterrows():
    earning_date = e_d['startdatetime']
    print(earning_date)
    trading_start = earning_date - 30 * US_BUSINESS_DAY
    trading_end = earning_date + 7 * US_BUSINESS_DAY
    df = web.DataReader('aapl', 'yahoo', trading_start, trading_end)
    df.drop(['High','Low','Open','Volume','Adj Close'], axis = 1,inplace = True)
    df_transposed = df.T
    num_cols = len(df_transposed.columns)
    print(f"trading_start={trading_start}, trading_end={trading_end}, # of columns: {num_cols}")
    if num_cols != 38:
        print(f"Encountered {num_cols} trading days")
        # this can be due to variety of reasons
        # Stock market was closed due to Hurricane Sandy on 10/29 - 10/30/2012 for example.
        # The Christmas holidays for 2010-12-02 -> 2011-01-27 has one trading day etc.
        # TODO: determine whether to recalculate the trading_start and trading_end dates based on the results
        #       or find a more reliable method of calculating -30< Earnings dates < +7
        print(df_transposed)
    range_end = -30 + num_cols
    df_transposed.columns = ['{}'.format(i) for i in range(-30,range_end)]
    frames.append(df_transposed)
result = pd.concat(frames)
print(result)