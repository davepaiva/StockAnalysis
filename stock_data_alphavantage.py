#Import all neccessary libraries
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import datetime as dt
from pytz import timezone
import pandas as pd



sym= input('Stock Ticker') #Enter the ticker for respective stock

ts = TimeSeries(key='Alpha Vantage API Key', output_format= 'pandas') #create time-series object
ti = TechIndicators(key='Alpha Vantage API Key', output_format= 'pandas') #create technical indicators onject


histdata, meta_data = ts.get_intraday(symbol=sym,interval='1min', outputsize='full') #get histroical data from time-series obj

# To change the timezone to local timezone, since all info is in reference to US/Eastern timezone.
histdata= histdata.reset_index() #remove the index of dataframe
x = histdata.date.tolist()       #put all the dates in a list to iterate over them and convert them one by one  
l = int(len(x))                  #get the length of the list to iterate in a FOR loop

#FOR loop to change the timezone to local timezone 
for i in range(l):
    x[i]= dt.datetime.strptime(x[i], "%Y-%m-%d %H:%M:%S") #Convert string datetime info into actual datetime objects so we can carry out the necessary datetime manipulations
    x[i] = timezone('US/Eastern').localize(x[i])  #Turns a naive datetime object into a timezone aware datetime object
    x[i]  = x[i].astimezone(timezone('Asia/Kolkata'))  #Convert the time in local timezone, in this case local timezone is Asia/Kolkata
    
    
histdata['datetime']= x  #put bcak the converted localised datetime objects back into the dataframe under new column 'datetime'
del histdata['date']     #Delete the original date column 


histdata.set_index('datetime')  #Set  the datetime column as the index for better access
