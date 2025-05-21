#except 45*3, 56+9, 56/6 all calculations will be correct

print("Enter the first number:", end = " ")
num_1 = int(input())
print("Enter the second number:", end = " ")
num_2 = int(input())
print("What operation do you want to perform? Enter:", end = " ")
operand = input()

if (operand == "+" and num_1 == 56 and num_2 == 9):
    print("77")
elif (operand == "*" and num_1 == 45 and num_2 == 3):
    print("555")
elif (operand == "/" and num_1 == 56 and num_2 == 6):
    print("4")
elif (operand == "+"):
    print(num_1 + num_2)
elif (operand == "-"):
    print(num_1 - num_2)
elif (operand == "*"):
    print(num_1 * num_2)
elif (operand == "/"):
    print(num_1/num_2)
else:
    print("Invaldi operation")