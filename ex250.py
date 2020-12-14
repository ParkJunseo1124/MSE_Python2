#!/usr/bin/env python
# coding: utf-8

# In[1]:

#range 함수는 정수만을 나타내기 때문에 이 경우에는 사용할 수 없다
#소수단위를 나타내기 위해 numpy.arange를 사용한다
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)

