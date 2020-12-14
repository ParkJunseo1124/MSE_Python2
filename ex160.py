#!/usr/bin/env python
# coding: utf-8

# In[1]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']


# In[3]:

#split함수를 사용해 .을 기준으로 문자열을 분리한 후 다음에오는 문자가 만약 h 또는 c일때 출력하기 위해 논리 연산자 or을 사용한다 
for i in 리스트:
  split = i.split(".")
  if (split[1] == "h") or (split[1] == "c"):
    print(i)

