"""import time"""
import csv
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
def get_running_processes():
    """get running process"""
    processes = []
    for process in psutil.process_iter(['pid', 'name']):
        processes.append(process.info)
    return processes

def count_processes(processes):
    """count process"""
    process_c = {}
    for process in processes:
        name = process['name']
        process_c[name] = process_c.get(name, 0) + 1
    return process_c

def save_to_csv(process_c):
    """save to csv file"""
    with open('processes_info.csv', 'w', newline='',encoding="utf-8") as csvfile:
        fieldnames = ['Process Name', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for process_name, count in process_c.items():
            writer.writerow({'Process Name': process_name, 'Count': count})

try:
    # 1. Get the list of all running processes
    running_processes = get_running_processes()

    # 2. Count the occurrence of each running process
    process_count = count_processes(running_processes)

    # 3. Store the information in a CSV file
    save_to_csv(process_count)

    print("Process information saved to processes_info.csv successfully.")
except ImportError as e:
    print("An error occurred:", e)
