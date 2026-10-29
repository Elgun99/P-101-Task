price = float(input("Sifariş məbləğini qeyd edin:"))
if price > 0:
    if price >= 200:
        discount = price * 0.2
    elif 100 <= price < 200:
        discount = price * 0.1
    else:
        discount = 0

else:
    print("Xəta: Məbləğ sıfırdan böyük olmalıdır.") 

print(f"Endirim: {discount}")

