"""import time"""
import time
import psutil
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
def monitor_aplliaction():
    """monitor application"""
    app_counts = {}
    for proc in psutil.process_iter(['name']):
        app_name = proc.info['name']
        if app_name in app_counts:
            app_counts[app_name] += 1
        else:
            app_counts[app_name] = 1
    for app_name, count in app_counts.items():
        if count > 2:
            print(f"Warning: More than 2 instances of {app_name} running!")
monitor_aplliaction()
