#!/usr/bin/env python
# coding: utf-8

# In[2]:


class OMG : 
    def print() :
        print("Oh my god")


# In[3]:

#현재 def print함수에 인자가 없는 상황인데 아래의 함수로 인해 인자가 넘어가 오류가 발생한다
#def print에 self를 적어야 한다
myStock = OMG()
myStock.print()     #OMG.print(mystock)

