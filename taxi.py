km=float(input("Səyahət məsafəsini km ilə qeyd edin:"))
saat=float(input("Səyahət vaxtını saat (0-23) ilə qeyd edin:"))
price=2+km*0.80
if saat >= 23 or saat < 6:
    price=price*1.2
if price > 3:
    price=3
print("price:",round(price,3),"AZN")
