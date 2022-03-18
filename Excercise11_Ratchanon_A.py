inputNumber = int(input("Number :"))


for x in range(inputNumber):

    air = (inputNumber - (x + 1)) * " "
    star = "*" * ((x + 1) + x)

    print(air, star)
