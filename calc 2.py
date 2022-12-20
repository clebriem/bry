

while True:
    print("select an action of your choice")
    print("1. addition")
    print ("2. subtraction")
    print("3.divide")
    print("4.multiplication")
    print("press q key to exit")

    choice = input ("enter your choice")

    if choice== 'q' :
        break

    num1 = float(input("enter"))
    num2 = float(input("enter"))

    if choice == '1':
        print(num1+num2)
    elif choice == '2':
       print (num1-num2)

    elif choice =='3':
       if num1 > num2:
           print (num1/num2)
        #elif num2 >num1:
            #print (num2/num1)
            
    elif choice =='4':
        print (num1*num2)
        
