import time

def run_clock():
    print("--- Clock Mechanics Theory Engine ---")
    print("Status: Active and Monitoring Time Cycles")
    try:
        while True:
            # Capturing the flow of time
            current_pulse = time.strftime("%H:%M:%S")
            print(f"Current Pulse: {current_pulse}", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProcess Interrupted. Time stands still.")

if __name__ == "__main__":
    run_clock()
