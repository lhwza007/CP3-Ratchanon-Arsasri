username = input("ID :")
userpass = input("PASS :")

if username == "lhwza007" and userpass == "mark12345":
    print("---Login Successfully---")

    print("-----------MarkShop-----------")
    print("1. Pepsi            :   17 THB")
    print("2. Coke             :   15 THB")
    print("3. LemonGreenTea    :   20 THB")
    print("4. MilkHoney        :   20 THB")
    print("5. Water            :    5 THB")
    print("------------------------------")

    order = int(input("Please select your order :"))
    howMany = int(input("How many?"))

    if order == 1:
        print("total amount :",17*howMany,"THB")
    elif order == 2:
        print("total amount :",15*howMany,"THB")
    elif order == 3:
        print("total amount :",20*howMany,"THB")
    elif order == 4:
        print("total amount :",20*howMany,"THB")
    elif order == 5:
        print("total amount :",5*howMany,"THB")

        print("Thank you")
    else:
        print("Error to try again :(")

        
else:
    print("!!! Username or password is incorrect !!!")