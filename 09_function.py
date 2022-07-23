def func():
    print("안녕하세요")
    print("파이썬과 40개의 작품들입니다.")
func()

def funcAdd(a,b):
    add=a+b
    return add
c=funcAdd(2,3)
print(c)

def funcMux(a,b):
    mux=a*b
    return mux
c=funcMux(2,3)
print(c)

def funcAddMux(a,b):
    add=a+b
    mux=a*b
    return add,mux
a,b=funcAddMux(1,3)
print(a,b)

def funcAddMux(a,b):
    add=a+b
    mux=a*b
    return add,mux
_,b=funcAddMux(1,3)
print(b)
