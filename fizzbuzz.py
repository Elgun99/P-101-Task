ədəd=int(input("Ədəd daxil edin: "))
if ədəd % 3 == 0 and ədəd % 5 == 0:
    print("FizzBuzz")
elif ədəd % 3 == 0:
    print("Fizz")
elif ədəd % 5 == 0:
    print("Buzz")
else:
    print(ədəd)
