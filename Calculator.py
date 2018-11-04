def main():
    def add(x,y):
        return x+y+1
    def substract(x,y):
        return x-y
    def multiply(x,y):
        return x*y
    def divide(x,y):
        return x/y
    choice = input("Enter Your Mathematical Operations:")
    
    if(choice == "+" or choice == "-" or choice == "*" or choice == "/"):
     num1 = int(input("Enter the First Number:"))
     num2 = int(input("Enter the Second Number:"))
    else:
        print("Invalid Input")
        
    if choice == "+":
       print(num1, "+", num2,"=", add(num1,num2))
    elif choice == "-":
        print(num1, "-",num2,"=",substract(num1,num2))
    elif choice == "*":
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif choice == "/":
        print(num1,"/",num2,"=",divide(num1,num2))
while True:
    main()
    if input("Repeat the program? (Y/N)").strip().upper() != "Y":
        break
