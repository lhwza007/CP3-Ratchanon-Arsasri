def login():
    userid = input("Id :")
    userpass = input("Pass :")

    while userid != "lhwza007" or userpass != "12345":
        print("Pleas try again")
        userid = input("Id :")
        userpass = input("Pass :")

    print("Login Success")



def showMenu():
    print("----------MarkShop----------")
    print("1. Vat calculator")
    print("2. Price calculator")



def selectMenu():
    inputForMenu = int(input("Select the menu >>"))

    while inputForMenu != 1 and inputForMenu != 2 :
        print("Error ")
        inputForMenu = int(input("Pleas select the menu again >>"))
    if inputForMenu == 1 :
        print("Price including tax : ", (vatCalculator(int(input("How much :")))))
    elif inputForMenu == 2 :
        print(priceCalculator())



def vatCalculator(total):
    vat = 7
    totalPrice = total + (total * 7 / 100)
    return totalPrice

def priceCalculator():
    userInputRound = int(input("How many item :"))
    sum = 0  # ผลรวม กำหนดไว้ก่อน

    for x in range(userInputRound):
        inputNumber = int(input("Item " + str(x + 1) + " :"))
        sum += inputNumber
    print("Price :", sum)
    print("Price including tax : :", vatCalculator(sum))


#login
#showmenu
#selectMenu
#vatCalculator
#priceCalculator

print(login())
print(showMenu())
print(selectMenu())
