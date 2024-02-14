import psutil
import csv

def get_running_processes():
    processes = []
    for process in psutil.process_iter(['pid', 'name']):
        processes.append(process.info)
    return processes

def count_processes(processes):
    process_count = {}
    for process in processes:
        name = process['name']
        process_count[name] = process_count.get(name, 0) + 1
    return process_count

def save_to_csv(process_count):
    with open('processes_info.csv', 'w', newline='') as csvfile:
        fieldnames = ['Process Name', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for process_name, count in process_count.items():
            writer.writerow({'Process Name': process_name, 'Count': count})

try:
    # 1. Get the list of all running processes
    running_processes = get_running_processes()

    # 2. Count the occurrence of each running process
    process_count = count_processes(running_processes)

    # 3. Store the information in a CSV file
    save_to_csv(process_count)

    print("Process information saved to processes_info.csv successfully.")
except Exception as e:
    print("An error occurred:", e)