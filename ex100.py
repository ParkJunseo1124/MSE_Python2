#!/usr/bin/env python
# coding: utf-8

# In[1]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]


# In[2]:

#같은 길이의 리스트를 같은 인덱스끼리 잘라 리스트로 반환시키는 역할을 하는 zip함수를 이용해 인덱스들을 묶어준 후 결과값을 dict함수를 사용하여 딕셔너리로 바꿔준다    
close_table = dict(zip(date, close_price))
print(close_table)

