import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2011, 2021)
business = [1780, 1800, 1700, 1865, 1950, 2000, 2000, 2130, 2180, 2200]
engineering = [1605, 1750, 1770, 1500, 1850, 2000, 2050, 2050, 2100, 2120]
logistics = [1400, 1420, 1350, 1400, 1450, 1560, 1630, 1785, 1820, 1850]

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].plot(years, business, color='red', marker='o')
axs[0].set_title('Business')
axs[0].grid(True)

axs[1].plot(years, engineering, color='blue', marker='s')
axs[1].set_title('Engineering')
axs[1].grid(True)

axs[2].plot(years, logistics, color='green', marker='^')
axs[2].set_title('Logistics')
axs[2].grid(True)

for ax in axs:
    ax.set_xlabel('Year')
    ax.set_ylabel('Enrollment')

plt.tight_layout()
plt.show()