def add(x,y):
    return x + y

def sub(x,y):
    return x - y


print("Select Operation.")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    #take input from user
    choice = input("Enter a choice(1/2/3/4)")

    # check choice if one of the four
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter a number: "))
        except ValueError:
            print("Invalid value: enter a number: ")
            continue

        if choice == '1':
            print(num1," + ",num2," = ", add(num1,num2))
        elif choice == '2':
            print(num1," - ",num2," = ",sub(num1,num2))
        elif choice == '3':
            print(num1," * ",num2," = ",mul(num1,num2))
        elif choice == '4':
            print(num1," / ",num2," = ",div(num1,num2))
        
        next_calculation = input("Enter for next calculation(yes/no): ")

        if next_calculation == "no":
            break
        else:
            print("invalid input")