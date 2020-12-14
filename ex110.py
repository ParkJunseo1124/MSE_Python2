#!/usr/bin/env python
# coding: utf-8

# In[1]:

#첫번째 if문에서 참이므로 조건을 만족시켜 if문으로 이동되고 if False문은 거짓이므로 else문으로 이동되어 최종적으로 3이 출력된다. 이후 남은 함수인 print("5")으로 인해 5가 출력된다
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")

