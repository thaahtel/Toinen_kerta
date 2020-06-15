yritykset = 1

tunnus = int(input("PIN-koodi: "))
if tunnus == 4321:
    print("Oikein, tarvitsit vain yhden yrityksen!")

elif tunnus != "4321":
    while tunnus != "4321":
        print("Väärin")
        tunnus = input("PIN-koodi: ")
        yritykset += 1

    print("Oikein, tarvitsit " + str(yritykset) + " yritystä")