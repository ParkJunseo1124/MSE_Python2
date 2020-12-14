#!/usr/bin/env python
# coding: utf-8

# In[1]:

#문자열은 변경할 수 없는 자료형이기 때문에 출력값은 abcd가 나오고 replace 메서드를 사용했을 때에는 원본은 그대로 둔채 변경된 문자열 객체를 리턴해준다
string='abcd'
string.replace('b','B')
print(string)

