import datetime
import time

for i in range(10):
    # Get current date and time
    current_time = datetime.datetime.now()

    # Print current time
    print("Current time:", current_time.time())

    # Wait for 1 minute before the next iteration
    time.sleep(5)
