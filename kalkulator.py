print ("Witaj w kalkulatorze")

a = float(input("podaj pierwszą liczbe"))
b = float(input("podaj drugą liczbe"))
c = str(input(" + , - , * , / , ** , // , % "))
if (c == "+"):
    wynik = a + b
    napis = (" suma ")
    n = (" Twoja ")
elif (c == "-"):
    wynik = a - b
    napis = (" różnica ")
    n = (" Twoja ")
elif (c == "*"):
    wynik = a * b
    napis = (" iloczyn ")
    n = (" Twój ")
elif (c == "/"):
    wynik = a / b
    napis = ("iloraz")
    n = (" Twój ")
elif (c == "**"):
    wynik = a ** b
    napis = (" potęga ")
    n = (" Twoja ")
elif (c == "//"):
    wynik = a ** 0.5
    napis = (" pierwiastek ")
    n = (" Twój ")
elif (c == "%"):
    wynik = a % b
    napis = (" reszta z dzielenia ")
    n = (" Twoja ")
else :
        print ("wybrałeś coś innego niż działanie matematyczne . To są działania które możesz wybrać : + , - , * , / , ** , // , % ")

print ( n ,napis ," to = " , wynik)
