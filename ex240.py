#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#함수2를 실행하며 2에 10이더해져 12가 된 상태로 함수1로 리턴된다
#함수1은 숫자에 2를 더한 후 함수0으로 리턴시키므로 14가 되어 함수0으로 리턴된다
#마지막으로 함수0에서 14에 2가 곱해져 최종적으로 28이 실행된다
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

