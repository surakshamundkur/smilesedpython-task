temperatures = [25, 28, 32, 30, 27, 23, 21]

#1.	Find the highest temperature:
highest_temperature = max(temperatures)
print(f"Highest temperature: {highest_temperature} degrees")

#2.	Print the days (indices) with temperatures above 30 degrees:
print("Days with temperatures above 30 degrees:")
for i, temp in enumerate(temperatures):
    if temp >= 30:
        print(f"Day {i} (index {i}): {temp} degrees")

#3.	Create a new list with the last three days' temperatures:
last_three_days_temperatures = temperatures[-3:]
print(f"Last three days' temperatures: {last_three_days_temperatures}")

