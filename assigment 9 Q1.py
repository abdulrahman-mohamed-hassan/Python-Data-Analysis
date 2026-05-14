import numpy as np
import matplotlib.pyplot as plt

names = ['Amr', 'Mai', 'Aya', 'Sam', 'Ali', 'Ola', 'Bob', 'Lee']
marks = np.array([56, 78, 93, 42, 97, 85, 34, 86])

average_marks = np.mean(marks)
success_percentage = (np.sum(marks >= 50) / len(marks)) * 100

plt.figure(figsize=(8, 5))
plt.bar(names, marks, color='steelblue')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Students Marks')
plt.text(0, 95, f'Success percentage: {success_percentage:.1f} %\nAverage marks: {average_marks:.3f}')
plt.ylim(0, 100)
plt.tight_layout()
plt.show()