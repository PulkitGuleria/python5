# def add (x,y):
#     s=x+y
#     print(s)

# def sub(x,y):
#     d=x-y
#     print(d)
 
# def mul(x,y):
#     m=x*y
#     print(m)

# x=int(input("x: "))
# y=int(input("y: "))
# add(x,y)
# sub(x,y)
# mul(x,y)


# def helloworld():
#     print("Hello World")
#     print("Good morning")
#     print("Have a nice day")
#     print("The function ends")

def addavg(x,y):
    s=x+y
    avg=s/2
    return s, avg
def sub(x,y):
    s=x-y
    return s

def mul(x,y):
    s=x*y
    return s
a = int(input("a: "))
b = int(input("b: "))

sum,average=addavg(a,b)
subtraction=sub(a,b)
multiplication=mul(a,b)

print("sum, average:",(sum,average))