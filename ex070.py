#!/usr/bin/env python
# coding: utf-8

# In[1]:


data=[2,4,3,1,5,10,9]


# In[2]:

#리스트형의 메소드인 sort 함수는 리스트 원본값을 직접 수정하여 정렬시킨다.
data.sort()
print(data)


# In[4]:

#내장 함수인 sorted 함수는 리스트의 원본 값은 그대로 둔채로 생성된 정렬 값을 반환합니다
data=[2,4,3,1,5,10,9]
data2=sorted(data)
print(data2)

