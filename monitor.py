import psutil
import time
import datetime

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print("\n===== SYSTEM HEALTH MONITOR =====")
    print("Time:", datetime.datetime.now())
    print("CPU Usage:", cpu, "%")
    print("Memory Usage:", memory, "%")
    print("Disk Usage:", disk, "%")
    print("=================================")

    time.sleep(5)
