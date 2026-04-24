width = int(input("Enter the width: "))
height = int(input("Enter the height: "))
area = width * height
perimeter = 2 * (width + height)
if width == height:
    shape = "square"
elif width > height:
    shape ="horizontal"
else:
    shape = "vertical"
print("the area is: ",area)
print("the perimeter is: ",perimeter)
print("the shape is: ",shape)


devices = int(input("Enter the number of devices: "))
if devices == 3 or 4:
    print("Premium plan. The monthly subscription is 200 EGP")
elif devices == 2:
    print("Standard plan. The monthly subscription is 165 EGP")
elif devices == 1:
    print("Basic plan. The monthly subscription is 120 EGP")
else:
    print("Invalid plan. Disallowed number of devices")


units = int(input("Enter the units consumed (in KW): "))
if units <= 99:
    cost = units * 0.15
elif units <= 199:
    cost = units * 0.30
elif units <= 299:
    cost = units * 0.40
else:
    cost = units * 0.50
print("Your monthly consumption is",units,"and your total bill is",cost,"pounds")


salary = int(input("Enter employee salary: "))
years = int(input("Enter the years of service: "))
if 4 <= years < 8:
    bones = salary * 0.05
elif 8 <= years < 12:
    bones = salary * 0.10
elif years >= 12:
    bones = salary * 0.20
else:
    bones = 0
print("Bonus is",bones,"pounds")


num = int(input("Enter a number: "))
print("the absolute value of",num,"is",abs(num),)


Classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))
attendance = (classes_attended / Classes_held) * 100
print("Attendance is", attendance, )
if attendance >= 75:
    print("you can enter the final exam.")
else:
    print("you are not allowed to enter the exam.")


Classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))
attendance = (classes_attended / Classes_held) * 100
print("Attendance is", attendance, )
if attendance >= 75:
    print("you can enter the final exam.")
else:
    medical = input("do you have a medical exuse (Y/N):")
    if medical == "Y":
        print("you can enter the final exam.")
    else:
        print("you are not allowed to enter the exam.")


month = int(input("Enter the month: "))
if month in [3 , 4 , 5]:
    print("It is Spring!")
elif month in [6 , 7 , 8]:
    print("It is Summer!")
elif month in [9 , 10 , 11]:
    print("It is Autumn!")
elif month in [12 , 1 , 2]:
    print("It is Winter!")
else:
    print("Invalid Month")


day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
if month < 1 or month > 12 or day < 1 or day > 31:
    print("Invalid Date!")
elif (month == 3 and day >= 20) or (month in [4,5]) or (month ==6 and day <= 19):
    print("It is Spring!")
elif (month == 6 and day >= 20) or (month in [7,8]) or (month ==9 and day <= 21):
    print("It is Summer!")
elif (month == 9 and day >= 22) or (month in [10,11]) or (month ==12 and day <= 20):
    print("It is Autumn!")
elif (month == 12 and day >= 21) or (month in [1,2]) or (month ==3 and day <= 19):
    print("It is Winter!")
else:
    print("Invalid Date!")


print("Would you like a sandwich or a main dish?")
order_type = input("Enter 'S' for sandwich or 'M' for main dish: ")
menu = {
    "S": {
        "Cheese Burger": 20,
        "Double Cheese Burger": 25,
        "Fish Fillet": 30,
        "Chicken Fillet": 35
    },
    "M": {
        "Grilled Chicken": 70,
        "Mixed Grill": 120,
        "Fish & Shrimps": 180
    }
}
if order_type in menu:
    print("Choose an item:")
    for i, (item, price) in enumerate(menu[order_type].items(), 1):
        print(i,"." ,item,"-",price,"pounds")
    choice = int(input("Enter the number of your choice: ")) - 1
    selected_item = list(menu[order_type].keys())[choice]
    total_cost = menu[order_type][selected_item]
    extras = input("Would you like (Drink & Fries) for 20 pounds? (Y/N): ")
    if extras == "Y":
        total_cost += 20
    dine_in = input("Will you eat in the café? (Y/N): ")
    if dine_in == "Y":
        total_cost *= 1.12
    print("Your total bill is",total_cost,"pounds")
else:
    print("Invalid choice!")