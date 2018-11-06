def main():
    result =  ""
    n = input("If you want to Encrypt Message enter '1'\nIf you want to Dcrypt Message enter '2'\nEnter '0' to exit\n")
    if(n == "1" or n == "2"):
        n1 = input("Enter your message: ")
    elif(n == "0"):
        exit
    else:
        print("Invalid Input")

    if(n == "1"):
        for i in n1:
            result = result + chr(ord(i) +4)
        print(result.replace("$"," "))
        
    elif(n == "2"):
        n1 = n1.replace(" ","$")
        for i in n1:
            result = result + chr(ord(i) -4)
        print(result)
while True:
    main()
    if(input("you want to repeat this Program:(Y/N)").strip().upper() != "Y"):
        break


