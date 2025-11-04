from pathlib import Path
import time

def wait_for_file(file_path, timeout=60, check_interval=2):
    waited = 0
    prev_size = -1
    stable_count = 0

    while waited < timeout:
        if file_path.exists():
            size = file_path.stat().st_size
            if size == prev_size:
                stable_count += 1
                if stable_count >= 3:  # stable for 3 checks
                    return True
            else:
                stable_count = 0
            prev_size = size
        time.sleep(check_interval)
        waited += check_interval
    return False

