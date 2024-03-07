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
def occurence_charcters(string_input):
    """occurence of the charcters"""
    char_count = {}
    for char in string_input:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    for i in range(min(3, len(sorted_chars))):
        print(f"{sorted_chars[i][0]}: {sorted_chars[i][1]}")
input_string =input("enter any string ")
occurence_charcters(input_string)
