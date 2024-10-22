import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate random weather data

days = np.arange(1, 31)  # Days from 1 to 30
temperatures = np.random.randint(15, 40, size=30)  # Random temperatures between 15 and 40

# Step 2: Analyze the data
mean_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
variance_temp = np.var(temperatures)

# Step 3: Display the results
print(f"Average Temperature: {mean_temp:.2f} °C")
print(f"Highest Temperature: {max_temp} °C")
print(f"Lowest Temperature: {min_temp} °C")
print(f"Temperature Variance: {variance_temp:.2f}")

# Step 4: Plot the data
plt.figure(figsize=(10, 5))
plt.plot(days, temperatures, label="Temperature (°C)", color='b', marker='o')
plt.axhline(mean_temp, color='r', linestyle='--', label=f"Mean Temp: {mean_temp:.2f}°C")
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over 30 Days')
plt.legend()
plt.grid(True)
plt.show()
