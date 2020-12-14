#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#message3을 출력하는 것이 목적이므로 def message3(): 이 적용된다. 
#for루프가 총 3번 반복될 것이고 그 말은 message2와 print("c")가 각각 3번씩 적용된다. 
#따라서 B와 C가 3번씩 반복해 출력된 후 message1()에 따라 A가 출력될 것이다 

def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

