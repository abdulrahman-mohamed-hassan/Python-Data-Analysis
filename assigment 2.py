num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
sum_result = num1 + num2 + num3
product_result = num1 * num2 * num3
average_result = sum_result / 3
print("The sum is", sum_result)
print("The product is", product_result)
print("The average is", average_result)


name = input("What is your name? ")
birth_year = int(input("On which year, were you born? "))
current_year = 2025
age = current_year - birth_year
print(name, "you are", age, "years old")


width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
area = width * height
perimeter = 2 * (width + height)
print("The area is:", area)
print("The perimeter is:", perimeter)


celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (9/5 * celsius) + 32
print(celsius, "Celsius is equivalent to", fahrenheit, "Fahrenheit")


radius = float(input("Please enter the radius: "))
diameter = 2 * radius
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius
print("The diameter is", diameter)
print("The area is", area)
print("The circumference is", circumference)


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
arithmetic_mean = (x + y) / 2
harmonic_mean = 2 / ((1/x) + (1/y))
print("Arithmetic Mean: ", arithmetic_mean)
print("Harmonic Mean: ", harmonic_mean)


apples = int(input("Enter the number of apples: "))
dozens = apples // 12
remaining = apples % 12
print(apples, "apples contain", dozens, "dozens and", remaining, "remaining apples.")


meters = int(input("Enter the distance in meters: "))
kilometers = meters // 1000
remaining_meters = meters % 1000
print(meters, "meters are equivalent to", kilometers, "kilometers and", remaining_meters, "meters.")


minutes = int(input("Enter a period of time (in minutes): "))
days = minutes // (24 * 60)
remaining_minutes = minutes % (24 * 60)
hours = remaining_minutes // 60
minutes_left = remaining_minutes % 60
print(minutes, "minutes make", days, "days,",hours, "hours, and" ,minutes_left, "minutes")


date = int(input("Enter the date in the format of (yyyymmdd): "))
year = date // 10000
month = (date % 10000) // 100
day = date % 100
print("The date is:" ,day," / ",month," /" ,year,)