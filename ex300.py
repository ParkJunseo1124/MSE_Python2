#!/usr/bin/env python
# coding: utf-8

# In[2]:

#세숫자 모두 try에 의해 변환이 시도되며 에러가 없을 경우에 else로 넘어가 "clean data"가 출력되고 공백문자열은 변환과정에서 에러가 발생하여 except로 넘어가 0이 츌력된다
#finally는 예외와 상관없이 항상 수행하는 코드이므로 세 숫자 모두 끝에 "변환 완료"가 출력된다.
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")

