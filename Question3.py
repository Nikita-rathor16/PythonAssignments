import psutil
 
def monitor_aplliaction():
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