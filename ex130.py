#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']


# In[2]:


#소수로 변환해주는 기능을 가진 float함수를 이용해 btc 딕셔너리 안의 시가, 종가, 최고가, 최저가 등을 계산한다
변동폭 = float(btc['max_price'])-float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭)>최고가:
    print("상승장")
else:
    print("하락장")

