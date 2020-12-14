#!/usr/bin/env python
# coding: utf-8

# In[1]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]


# In[3]:

#반복운의 범위가 low_prices의 전체 길이만큼이므로 모든 인덱스에서의 변동폭을 volatility에 대입한다
volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)

