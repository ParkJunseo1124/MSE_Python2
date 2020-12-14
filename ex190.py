#!/usr/bin/env python
# coding: utf-8

# In[1]:


apart = [ [101, 102], [201, 202], [301, 302] ]


# In[3]:

#첫번째 for문을 이용해 묶여있는 리스트끼리 분리한 후 두번째 for문으로 호를 붙여 정혛한다 작업완료 후 - 5개를 출력한다
for 층 in apart:
    for 집 in 층:
        print(집, "호")
print("-" * 5)

