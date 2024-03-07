"""import time"""
import time
def log_execution_time(func):
    """log exceution"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        with open("execution_logs.txt", "a",encoding="utf-8") as f:
            f.write(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds\n")
        return result
    return wrapper
@log_execution_time
def fib_series(n):
    """Generate Fibonacci series up to n"""
    fib_serie = []
    a, b = 0, 1
    for _ in range(n):
        fib_serie.append(a)
        a, b = b, a + b
    return fib_serie
num = int(input("Enter the number: "))
if num <= 0:
    print("Enter a positive number.")
else:
    res = fib_series(num)
    print("Fibonacci series:", res)
