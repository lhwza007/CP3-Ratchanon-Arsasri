def vatCalcilator (totalPriceVat):
    totalPriceVat =  totalPriceVat + (totalPriceVat * 7 / 100)
    return totalPriceVat

inputPrice = int(input("Price of your item :"))        #ให้ใส่ราคา

print("price including tax :",vatCalcilator(inputPrice))   #ปริ้นราคารวมภาษี