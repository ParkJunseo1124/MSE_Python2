#!/usr/bin/env python
# coding: utf-8

# In[1]:

#a에 200, b에 100을 명시적으로 적어주었으므로 순서에 상관없이 결과값이 나타난다
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

