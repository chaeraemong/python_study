for i in range(7):
    print(i)

for i in range(5,10):
    print(i)

for i in range(10, 5, -1):
    print(i)

a_list=[1,2,3,4,5,"안녕", "하세요"]
for i in a_list:
    print(i)

a_str="hello python"
for i in a_str:
    print(i)

name_list=["홍길동", "장영희", "김철수"]
age_list=[500, 5, 12]
for i,k in enumerate(name_list):
    print("i=",i,end=' ')
    print("k=", k)

name_list=["홍길동", "장영희", "김철수"]
age_list=[500, 5, 12]
for i,k in enumerate(name_list):
    print(k,end=' ')
    print(age_list[i])
for i,k in enumerate(name_list):
    print(name_list[i],end=' ')
    print(age_list[i])

name_list=["홍길동", "장영희", "김철수"]
age_list=[500, 5, 12]
for i in range(len(name_list)):
    print(name_list[i],end=' ')
    print(age_list[i])

test_list=[i for i in range(10)]
print(test_list)
test2_list=[]
for i in range(10):
    test2_list.append(i)
print(test2_list)

test_list=[i*5 for i in range(10)]
print(test_list)
test2_list=[0 for i in range(10)]
print(test2_list)

a=0
while a<5:
    print(a)
    a=a+1

a=0
while True:
    print(a)
    a=a+1
    if a>=5:
        break
