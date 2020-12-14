#!/usr/bin/env python
# coding: utf-8

# In[1]:

#elif는 '만약 ~이 아니라면 ~하라'의 뜻을 가지고 있으므로 a가 b보다 크고 c보다도 크면 if문이 적용, 그렇지 않다면 elif문이 적용된다
def print_max(a, b, c):
    if a>b and a>c:
        print(a)
    elif b>c and b>a:
        print(b)
    else:
        print(c)

