a=1
b=1
if a==b:
    print("두 개의 값은 동일")
if a!=b:
    print("두 개의 값은 다름")

a=1
b=2
if a==b:
    print("두 개의 값은 동일")
else:
    print("두 개의 값은 다름")

a=1
b=2
if a>b:
    print("a 값이 더 큼")
elif a<b:
    print("b 값이 더 큼")
else:
    print("두 개의 값은 동일")

a=1
b=1
if a>=b:
    print("a 값이 더 크거나 같음")
if a<=b:
    print("b 값이 더 크거나 같음")

a=1
b=1
c=2
d=2
if a==b and c==d:
    print("두 조건 모두 만족")
if a==b or c==d:
    print("두 조건 중 하나라도 만족")

a_str="hello python"
if a_str=="hello python":
    print("hello python 문자열이 동일")
if a_str=="hi python":
    print("hi python 문자열이 동일")
if "hello" in a_str:
    print("hello가 포함되어 있음")
if "hello" not in a_str:
    print("hello가 포함되어 있지 않음")
if "hi" in a_str:
    print("hi가 포함되어 있음")
if "hi" not in a_str:
    print("hi가 포함되어 있지 않음")

a_list=["안녕", 1, 2, "파이썬"]
if "안녕" in a_list:
    print("a_list에 '안녕'이 포함되어 있음")
if 2 in a_list:
    print("a_list에 숫자 2가 포함되어 있음")

a_list=["안녕", 1, 2, "파이썬"]
if "안녕" not in a_list:
    print("a_list에 '안녕이 포함되어 있지 않음")
if 5 not in a_list:
    print("a_list에 숫자 5는 없음")
