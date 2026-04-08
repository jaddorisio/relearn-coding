import time

loading_symbols = ["|","/","-","\\"]
print("Starting the countdown...")

# We use range(5, 0, -1) to count backwards from 5 down to 1
for i in range(10, 0, -1):
    # \r moves the cursor to the far left. 
    # end="" stops print from moving to the next line.
    
    
    print(f"\rTime remaining: {i} seconds {loading_symbols[i%4]} ", end="")

    
    # Pause for 1 second so we can see it
    time.sleep(1)

# A final print to clear the line and finish
print("\rBOOM!                              ")   