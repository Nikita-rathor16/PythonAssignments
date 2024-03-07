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
def reverse(input_string):
    """return reverse function"""
    words = input_string.split()
    reversed_words = words[::-1]
    reverse_string = ' '.join(reversed_words)
    return reverse_string
user_input = input("Enter a string: ")
REVERSE_STRING = reverse(user_input)
print("Reversed string:", REVERSE_STRING)
