# Home Can you create a Program I will give you number(userinput and print table)
#
# User input - num int -> 10, 100, -1, 2, 3.14 -> input
# 9x1 = 9
# 9x2 = 18... till 10

num = int(input("Please enter number for multipliation table\n"))
print("no is : ", num)

for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result} ")


