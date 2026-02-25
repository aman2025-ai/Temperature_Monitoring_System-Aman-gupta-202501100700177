 Case Study: Temperature Monitoring System
1️⃣ Problem Statement

Design a Python-based Temperature Monitoring System that simulates an IoT temperature sensor.

The system should:

Accept minimum and maximum temperature limits from the user.

Generate random temperature values every 2 seconds.

Compare the generated temperature with the defined limits.

Display appropriate alert messages:

Below minimum limit → Warning message

Above maximum limit → High temperature alert

Within range → Safe message

2️⃣ Approach

The following steps are used to solve the problem:

Step 1: Import Required Modules

random → To generate random temperature values

time → To create a 2-second interval

Step 2: Take User Input

Accept minimum temperature limit

Accept maximum temperature limit

Step 3: Start Monitoring Loop

Use while True to simulate continuous monitoring

Step 4: Generate Random Temperature

Use random.uniform(-10, 60)

This generates a floating-point temperature value

Step 5: Compare Temperature with Limits

If temperature < minimum limit → Display LOW alert

If temperature > maximum limit → Display HIGH alert

Otherwise → Display SAFE message

Step 6: Add Delay

Use time.sleep(2) to wait for 2 seconds before next reading
 4️⃣ Sample Output
Enter Minimum Temperature Limit: 20
Enter Maximum Temperature Limit: 40

Temperature Monitoring Started...

Current Temperature: 18.75 °C
⚠ ALERT: Temperature is BELOW Minimum Limit!

Current Temperature: 32.48 °C
✅ Temperature is within the safe range.

Current Temperature: 45.91 °C
🔥 ALERT: Temperature is ABOVE Maximum Limit
