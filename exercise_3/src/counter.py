import time

if __name__ == "__main__":
    counter = 1  # Start the counter at 1
    while True:
        print(f"Counter: {counter}", flush=True)  # Force flush after printing
        counter += 1  # Increment the counter
        time.sleep(2)  # Wait for 2 seconds before the next iteration
