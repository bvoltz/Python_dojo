import os
import sys
from datetime import datetime

# 1. Setup your data structure
tasks = ["clean_logs", "backup_db", "send_report"]
server_status = {"clean_logs": True, "backup_db": False, "send_report": True}


# 2. Get the current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. Safely read and write files
try:
    with open("daily_log.txt", "w") as file:
        file.write(f"Automation Initialize at {current_time}...\n")
        
        # 4. Loop and make decisions
        for task in tasks:
            if server_status.get(task) == True:
                log_msg = f"SUCCESS: {task} completed.\n"
            else:
                log_msg = f"ERROR: {task} failed.\n"
                
            file.write(log_msg)
            print(log_msg.strip())
            
# 5. Handle errors cleanly
except Exception as error:
    print(f"System Error: {error}")
    sys.exit(1)