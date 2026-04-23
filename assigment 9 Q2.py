import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2011, 2021)
business = [1780, 1800, 1700, 1865, 1950, 2000, 2000, 2130, 2180, 2200]
engineering = [1605, 1750, 1770, 1500, 1850, 2000, 2050, 2050, 2100, 2120]
logistics = [1400, 1420, 1350, 1400, 1450, 1560, 1630, 1785, 1820, 1850]

plt.figure(figsize=(10, 6))
plt.plot(years, business, marker='o', color='red', label='Business')
plt.plot(years, engineering, marker='s', color='blue', label='Engineering')
plt.plot(years, logistics, marker='^', color='green', label='Logistics')

plt.title("Student Enrollment Over 10 Years")
plt.xlabel("Year")
plt.ylabel("Number of Students")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()