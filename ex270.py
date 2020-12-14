#!/usr/bin/env python
# coding: utf-8

# In[19]:

#주식에 대한 정보를 저장하는 Stock클래스를 이용해 각각의 종목명에 따라 코드와 per에 해당하는 숫자를 입력하고 i.code, i.per을 이용해 출력한다
종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per) 

