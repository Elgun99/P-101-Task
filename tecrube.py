təcrübə=float(input("İş təcrübənizi qeyd edin:"))
bal=float(input("Balınızı qeyd edin:"))
if  təcrübə >=2 and bal >=70:
    print("Növbəti mərhələyə dəvət olunursunuz.")
elif bal >=90:
    print("Güclü namizəd.")
else:
    print("Namizəd uyğun deyil.")
if təcrübə < 0 or bal < 0:
    print("Xəta: Təcrübə və bal sıfırdan böyük olmalıdır.")