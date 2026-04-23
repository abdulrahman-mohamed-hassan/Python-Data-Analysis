def odd_1_to_9():
    print("Odd numbers between 1 and 9:")
    for i in range(1, 10, 2):
        print(i, end=' ')
    print()
odd_1_to_9()



def odd_m_to_n():
    m = int(input("Enter starting number (m): "))
    n = int(input("Enter ending number (n): "))
    print("Odd numbers between", m, "and", n, ":")
    for i in range(m, n+1):
        if i % 2 != 0:
            print(i, end=' ')
    print()
odd_m_to_n()



def month():
    number = int(input("Enter a month number (1-12): "))
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if 1 <= number <= 12:
        print("The month is: " + months[number - 1])
    else:
        print("Invalid month number")
month()



def grade():
    mark = int(input("Enter the student's mark (0-100): "))
    if 90 <= mark <= 100:
        print("Grade: Excellent")
    elif 80 <= mark <= 89:
        print("Grade: Very Good")
    elif 70 <= mark <= 79:
        print("Grade: Good")
    elif 60 <= mark <= 69:
        print("Grade: Satisfactory")
    elif 50 <= mark <= 59:
        print("Grade: Conditional Pass")
    elif 0 <= mark <= 49:
        print("Grade: Fail")
    else:
        print("Invalid Mark")
grade()



def fixed_figure():
    print("Fixed 5x10 star figure:")
    for _ in range(5):
        print('* ' * 10)
fixed_figure()



def variable_figure():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Star figure with", rows, "rows and", cols, "columns:")
    for _ in range(rows):
        print('* ' * cols)
variable_figure()



def product_of_three():
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    c = int(input("Enter third integer: "))
    result = a * b * c
    print("The product is:", result)
    return result
product_of_three()



def average_of_five():
    nums = []
    for i in range(1, 6):
        num = int(input("Enter integer " + str(i) + ": "))
        nums.append(num)
    avg = sum(nums) / 5
    print("The average is:", avg)
    return avg
average_of_five()



def absolute_value():
    n = int(input("Enter an integer: "))
    abs_val = abs(n)
    print("The absolute value is:", abs_val)
    return abs_val
absolute_value()



def square():
    n = float(input("Enter a number: "))
    sq = n * n
    print("The square is:", sq)
    return sq
square()



def min_of_three():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    z = float(input("Enter third number: "))
    minimum = min(x, y, z)
    print("The minimum is:", minimum)
    return minimum
min_of_three()



def sum_with_step():
    a = int(input("Enter start number (a): "))
    b = int(input("Enter end number (b): "))
    c = int(input("Enter step (c): "))
    series_sum = sum(range(a, b + 1, c))
    print("The sum is:", series_sum)
    return series_sum
sum_with_step()