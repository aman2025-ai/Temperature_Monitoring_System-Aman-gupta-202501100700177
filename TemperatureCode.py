# Temperature Monitoring System (IoT Simulation)

import random      # Random temperature generate karne ke liye
import time        # 2 second delay ke liye

# Taking minimum and maximum temperature limits from user
min_temp = float(input("Enter Minimum Temperature Limit: "))
max_temp = float(input("Enter Maximum Temperature Limit: "))

print("\nTemperature Monitoring Started...\n")

while True:
    # Generate random temperature between -10 and 60 degree Celsius
    current_temp = random.uniform(-10, 60)

    # Display current temperature (rounded to 2 decimal places)
    print(f"Current Temperature: {round(current_temp, 2)} °C")

    # Compare temperature with limits
    if current_temp < min_temp:
        print("⚠ ALERT: Temperature is BELOW Minimum Limit!\n")
    
    elif current_temp > max_temp:
        print(" ALERT: Temperature is ABOVE Maximum Limit!\n")
    
    else:
        print(" Temperature is within the safe range.\n")

    # Wait for 2 seconds before next reading
    time.sleep(2)
