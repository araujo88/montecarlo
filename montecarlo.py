import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import datetime

ticker = 'BTC'
file = pd.read_csv("BTC.csv", parse_dates=True)
date = pd.to_datetime(file.time)
data = file.close
#plt.plot(date, data)
#plt.show()

#log_returns = np.log(1 + data.pct_change())
#sns.distplot(log_returns.iloc[1:])
#plt.xlabel("Daily Return")
#plt.ylabel("Frequency")
#plt.show()

u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5*var)

stdev = log_returns.std()
days = 30
iterations = 10000
Z = norm.ppf(np.random.rand(days, iterations))
daily_returns = np.exp(drift + stdev * Z)

price_paths = np.zeros_like(daily_returns)
price_paths[0] = data.iloc[0]
for t in range(1, days):
    price_paths[t] = price_paths[t-1]*daily_returns[t]

base = date.iloc[0]
future_dates = [base + datetime.timedelta(days=x) for x in range(days)]

plt.plot(date, data, linestyle='dashed')
plt.plot(future_dates, price_paths)
plt.ylabel("Close price (BTC/USDT)")
plt.show()

#plt.hist(price_paths[-1,:], bins = 20)
#sns.set_style('darkgrid')
sns.histplot(price_paths[-1,:], bins = 20, stat = "frequency")
plt.xlabel("Close price (BTC/USDT)")
plt.ylabel("Frequency")
plt.show()