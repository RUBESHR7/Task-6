2)which one is greater and which one is less?
# 	ex:
# 	input1:12
# 	input2:14

# 	output:input1 is less than input2 and input2 is greater than input1

# 	ex:
# 	input1:16
# 	input2:14

# 	output:input2 is less than input1 and input1 is greater than input2

a=int(input("enter the First number: "))
b=int(input("enter the Second number: "))
if (a>b):
    print("The First number",a,"is greater than Second number",b,"and Second number",b,"is less than First number",a)
else:
    print("The Second number",b,"is greater than First number",a,"and First number",a,"is less than Second number",b)