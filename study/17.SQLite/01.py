import pandas as pd
import pandas_datareader.data as web
import datetime
import sqlite3

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 6, 12)
dr = web.DataReader("078930.KS", "yahoo", start, end)

con = sqlite3.connect("C:/Users/xjord/OneDrive/문서/GitHub/KSHTS/study/17.SQLite/kospi.db")
dr.to_sql('078930', con, if_exists='replace')

readed_dr = pd.read_sql("select * from '078930'", con, index_col='Date')