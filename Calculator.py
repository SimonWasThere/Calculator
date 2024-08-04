one = int(input("What is the first number? \n"))
two = int(input("\nWhat is the second number? \n"))

print("\nThe operator's that you can use is: add, sub, mult, div.\n")

operator = input("What operator do you want to use? \n")

add = one + two
sub = one - two
mult = one * two
div = one / two

if operator == "add":
	print("\n" + str(add))
elif operator == "sub":
	print("\n" + str(sub))
elif operator == "mult":
	print("\n" + str(mult))
elif operator == "div":
	print("\n" + str(div))
else:
	print("That's not an operator.")
