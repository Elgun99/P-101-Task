çəki=float(input("Çamadanın çəkisini qeyd edin:"))
növ=input("Bilet növünü qeyd edin (econom/business):")
if çəki < 23:
    print("Pulsuz çamadan daşınması mümkündür.")
elif çəki >= 23 and çəki <= 32:
    if növ == "econom":
        price=30
    print(f"Əlavə ödəniş: {price} AZN")
elif çəki <=32:
    if növ == "business":
        print("Pulsuz çamadan daşınması mümkündür.")
elif çəki > 32:
    print("Qəbul edilmir.")