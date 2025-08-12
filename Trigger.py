import schedule
import time
import subprocess
import sys
import random
import threading

def run_my_script():
    print(f"[{time.ctime()}] Running script...")
    subprocess.call([sys.executable, "main.py"])

    # Schedule the next run randomly
    next_hours = random.randint(3, 6)  # Run between 3 to 6 hours
    print(f"[{time.ctime()}] Next run scheduled in {next_hours} hours.")

    schedule.clear()  # Clear old job
    schedule.every(next_hours).hours.do(wrapper)

def wrapper():
    thread = threading.Thread(target=run_my_script)
    thread.start()

# Initial random delay
initial_delay = random.randint(1, 4)
print(f"Initial script will run in {initial_delay} hours.")
schedule.every(initial_delay).hours.do(wrapper)

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(60)
