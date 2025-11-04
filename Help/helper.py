from pathlib import Path
import time

import os
import time

def Waiter():
# Path to the target file
    download_dir = Path(r"C:\Users\a829052\Downloads")
    
    target_file_JSON = max(download_dir.glob("downloadsasd*.json"), key=lambda f: f.stat().st_mtime)
    
# Timeout in seconds
    timeout = 10
    start_time = time.time()
    
    while True:
        if os.path.exists(target_file_JSON):
            return True
            break
        elif time.time() - start_time > timeout:
            return False
            break



