# Kübra Endez 2012722
import pandas as pd
from pandas.plotting import autocorrelation_plot, lag_plot
import matplotlib.pylab as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df_brazil = pd.read_csv("sudeste.csv", usecols=["date", "temp"])
df_madrid = pd.read_csv("weather_madrid_LEMD_1997_2015.csv", usecols=["CET", "Mean TemperatureC"])

def prepare_brazil(df):
    temp = df.groupby("date").mean().reset_index()
    date_series = temp["date"]
    temp_series = temp["temp"]
    temp_series.index =  pd.DatetimeIndex(date_series)

    start_date, end_date = date_series.head(1).values[0], date_series.tail(1).values[0]
    date_indx = pd.date_range(start_date, end_date)
    result = temp_series.reindex(date_indx, fill_value=0)

    return result

def prepare_madrid(df):
    temp = df
    date_series = temp["CET"]
    temp_series = temp["Mean TemperatureC"]
    temp_series.index =  pd.DatetimeIndex(date_series)

    start_date, end_date = date_series.head(1).values[0], date_series.tail(1).values[0]
    date_indx = pd.date_range(start_date, end_date)
    result = temp_series.reindex(date_indx, fill_value=0)

    return result


b, m = prepare_brazil(df_brazil), prepare_madrid(df_madrid)

plt.plot(b)
plt.title("brazil")
plt.show()
plt.plot(m)
plt.title("madrid")
plt.show()

from statsmodels.tsa.stattools import adfuller
print("adfuller test of brazil")
print(adfuller(b.dropna()))
print("adfuller test of madrid")
print(adfuller(m.dropna()))

plt.hist(b.dropna())
plt.title("histogram of brazil")
plt.show()

plt.hist(m.dropna())
plt.title("histogram of madrid")
plt.show()

X = m.dropna().values
low, high = X[:len(X)//2], X[len(X)//2:]
print ("Madrid's low mean is ", low.mean(), "and high mean is", high.mean())
print ("Madrid's low variation is ", low.var(), "and high variation is", high.var())

X = b.values
low, high = X[:len(X)//2], X[len(X)//2:]
print ("Brazil's low mean is", low.mean(), "and high mean is", high.mean())
print ("Brazil's low variation is", (low.var()), "and high variation is", (high.var()))

autocorrelation_plot(b)
plt.title("Brazil autocorrelation")
plt.show()
autocorrelation_plot(m)
plt.title("Madrid autocorrelation")
plt.show()

lag_plot(b)
plt.title("Lag plot of Brazil")
plt.show()
lag_plot(m)
plt.title("Lag plot of Madrid")
plt.show()

# Brazil and Madrid datasets are both stationary and there is no increasing trends.
# This conclusion is reached by checking autocorrelation, lag, histogram and default plottings.
# In addition adfuller test is conducted for both datasets and their p-values are lower than 0.05
# To conclude there is global warming in both Brazil and Madrid

