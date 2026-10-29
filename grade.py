bal=float(input("Balınızı qeyd edin: "))
if bal >= 91 and bal <= 100:
    print("A")
elif bal >= 81 and bal <= 90:
    print("B")
elif bal >= 71 and bal <= 80:
    print("C")
elif bal >= 61 and bal <= 70:
    print("D")
elif bal >= 51 and bal <= 60:
    print("E")
elif bal >= 0 and bal <=50:
    print("F")
elif bal < 0 or bal > 100:
    print("Xəta: Yanlış bal.")