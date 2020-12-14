#!/usr/bin/env python
# coding: utf-8

# In[1]:

#super() 키워드를 통해서 부모클래스에 접근
#__init__() 부모클래스의 생성자를 명시적으로 호출
#자식클래스에 개체가 생성될 때 생성자가 호출이 되고 '자식생성'이 호출이 된 후 super를 통해 부모클래스에 접근, __init__으로 인해 '부모생성'이 호출된다
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()

