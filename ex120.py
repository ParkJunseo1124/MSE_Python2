#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}


# In[6]:

#input함수를 사용해 원하는 값을 입력하면 그에 따라 변수에 저장되게 한 후 그 값이 딕셔너리에 있다면 정답입니다가 없다면 오답입니다가 출력되게 한다
과일 = input("좋아하는 과일은?")
if 과일 in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")

