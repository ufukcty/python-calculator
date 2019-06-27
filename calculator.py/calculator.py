def add(x, y):
	return x + y
def subtrack(x, y):
	return x - y
def divide(x, y):
	return x / y
def multiply(x, y):
	return x * y


print("select operation")
print("1.add")
print("2.subtrack")
print("3.divide")
print("4.multiply")

select = input("select operation 1/2/3/4: ")

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

if select == "1":
	print(num1 ,"+", num2,  "=", add(num1, num2))

elif select == "2":
	print(num1 ,"-", num2, "=", subtract(num1, num2))

elif select == "3":
	print(num1, "/", num2, "=", divide(num1, num2))

elif select == "4":
	print(num1, "*", num2, "=", multiply(num1, num2))

else:
	print("false value")
