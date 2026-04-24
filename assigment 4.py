M = int(input("Enter the first number (M): "))
N = int(input("Enter the second number (N): "))
even_sum = sum(i for i in range(M, N+1) if i % 2 == 0)
print(f"The sum of even numbers between {M} and {N} is: {even_sum}")


total = 0
num = 0
while total <= 50:
    num += 1
    total += num
    print(num, total)


import math
x = int(input("Enter a number: "))
print("Number Factorial")
for i in range(1, x+1):
    print(i, math.factorial(i))


numbers = [i for i in range(1500, 2301) if i % 7 == 0 and i % 5 == 0]
print("The numbers are:", ", ".join(map(str, numbers)))


num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{i} X {num} = {i * num}")


grades = [int(input(f"Enter the grade of student ({i+1}): ")) for i in range(10)]
average = sum(grades) / len(grades)
print(f"The average grade is {average:.1f}")


num_students = int(input("Enter the number of students: "))
grades = [int(input(f"Enter the grade of student ({i+1}): ")) for i in range(num_students)]
average = sum(grades) / len(grades)
print(f"The average grade is {average:.1f}")


grades = []
while True:
    grade = int(input("Enter a grade: "))
    if 0 <= grade <= 100:
        grades.append(grade)
    else:
        break
if grades:
    print(f"The average grade is {sum(grades) / len(grades):.1f}")
else:
    print("No valid grades entered.")


loan_amount = int(input("Enter the loan amount: "))
interest_rate = float(input("Enter the interest rate: "))
print("\nMonth  Amount")
print("-" * 30)
for month in range(13):
    print(f"{month:<5} {int(loan_amount)}")
    loan_amount += loan_amount * interest_rate


num = int(input("Enter a number: "))
if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


num = input("Enter a number: ")
print(f"The number of digits is: {len(num)}")