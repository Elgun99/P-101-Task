yaş=float(input("Yaşınızı qeyd edin:"))
tələbə=input("Tələbə olub-olmadığınızı qeyd edin (bəli/xeyr):")
if yaş < 7:
    print("Siz pulsuz bilet əldə edə bilərsiniz.")
elif yaş < 65:
    price=4
elif tələbə == "bəli":
    price=5
print(f"Bilet qiyməti: {price} AZN")
