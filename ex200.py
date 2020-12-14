#!/usr/bin/env python
# coding: utf-8

# In[1]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]


# In[7]:

# total_profit += profit 은   total_profit  = total_profit + profit와 같다 1일차부터 시가와 종가의 차이를 계산
total_profit=0
for day_price in ohlc[1:]:
    profit = day_price[0] - day_price[3]
    total_profit += profit

