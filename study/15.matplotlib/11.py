import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import mplfinance

start = datetime.datetime(2016,3,1)
end = datetime.datetime(2016,3,31)
skhynix = web.DataReader("000660.KS", "yahoo", start, end)

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

mplfinance.plot(skhynix, type='candle', style='starsandstripes')

plt.show()