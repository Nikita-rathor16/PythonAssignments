def fibonacci(n):
    fib_series=[]
    a,b=0,1
    for e in range(n):
        fib_series.append(a)
        a,b=b,a+b
    return fib_series
num=int(input("enter the number  "))

if num<=0:
   print("enter postive number")
else:
    result=fibonacci(num)
    print("fibonacci series ",result)
