for i in range(5):
    print("*" * 10)


for i in range(4):
    print("*+*+*+*+")


for i in range(3):
    print("12345678")
    print("XXXXXXXX")


for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("X", end="")
        else:
            print("O", end="" )
    print()


for i in range(1, 9):
    print("*" * i)


for i in range(8, 0, -1):
    print("X" * i)


x = 1
while x <= 10:  
    y = 1
    while y <= x:  
        print(y % 10, end="")  
        y += 1
    print()  
    x += 1

          
for i in range(1, 6):  
    print("*" * i)
for i in range(4, 0, -1):  
    print("*" * i)


num = int(input("Enter a number: "))  
for i in range(1, 11):
     print(str(num) , " x " + str(i) , " = " , str(num * i))


print("""
++*++*++*+
++*++*++*+
++*++*++*+
""")


print("""
****
****
****
****
****
****
****
****
****
****
****
****
****
****
****
""")


print("""
**********
*********
********
*******
******
*****
****
***
**
*
""")


print("""
1234567890
123456789
12345678
1234567
123456
12345
1234
123
12
1
""")