# This function adds two numbers
def add(x, y):
    return x + y
# This function subtracts two numbers
def subtract(x, y):
    return x - y
# This function multiplies two numbers
def multiply(x, y):
    return x * y
# This function divides two numbers
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    # take input from the user
    o = input("Enter o(1/2/3/4): ")
    # check if o is one of the four options
    if o in ('1', '2', '3', '4'):
        try:
            n = float(input("Enter first number: "))
            m = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if o == '1':
            print(n,"+",m,"=",add(n, m))
        elif o == '2':
            print(n,"-",m,"=",subtract(n, m))
        elif o == '3':
            print(n,"*",m,"=",multiply(n, m))
        elif o == '4':
            print(n,"/",m,"=",divide(n, m))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (1/0): ")
        if next_calculation == "0":
          break
    else:
        print("Invalid Input")