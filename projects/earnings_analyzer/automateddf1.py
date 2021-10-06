import pandas as pd
from datetime import date
from datetime import timedelta
from yahoo_earnings_calendar import YahooEarningsCalendar
import dateutil.parser
from pandas_datareader import data as web
import yahoo_fin.stock_info as si

start = date(2008, 3, 11)
start_date = pd.to_datetime(start)
end = date(2021, 7, 27)
end_date = pd.to_datetime(end)


TICKER = 'AAPL'
aapl_earnings_hist = si.get_earnings_history(TICKER)
frame = pd.DataFrame.from_dict(aapl_earnings_hist)
frame['startdatetime'] = pd.to_datetime(frame['startdatetime'])
frame['startdatetime'] = frame['startdatetime'].dt.date

frame_filtered = frame[frame['startdatetime'] >= start]
frame_filtered = frame_filtered[frame_filtered['startdatetime'] <= end]
print(frame_filtered)
earningsdate_final = frame_filtered.drop(['ticker','companyshortname','startdatetimetype','epsestimate','epsactual','epssurprisepct','timeZoneShortName','gmtOffsetMilliSeconds','quoteType'], axis = 1)

print(earningsdate_final)
  
print(earningsdate_final.shape)





# print(frame)

# print(earnings_df)


# df = web.DataReader('aapl', 'yahoo', start, end)

# print(df)
