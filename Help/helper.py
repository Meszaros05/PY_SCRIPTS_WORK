from pathlib import Path
import time
import os
import time

def Waiter():
    # Path to the target file
    download_dir=""
    # Timeout in seconds
    timeout = 5
    start_time = time.time()
    
    while True:
        files=list(download_dir.glob()) #ide kell a file neve
        
        if files:
            target_file = max(files, key=lambda f: f.stat().st_mtime)
            return target_file  # Return the file path when found

        if time.time() - start_time > timeout:
            return None  # Timeout, no file found

        time.sleep(1)



