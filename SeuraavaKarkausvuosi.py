# Kirjoita ratkaisu tähän
vuosi = int(input("Anna vuosi: "))
muuttuja = vuosi


if vuosi % 4 != 0:

    while muuttuja % 4 != 0:
        muuttuja = muuttuja + 1

    if (muuttuja) % 400 == 0:
        print("Vuotta " + str(vuosi) + " seuraava karkausvuosi on " + str(muuttuja))

    elif (muuttuja) % 100 == 0:
        print("Vuotta " + str(vuosi) + " seuraava karkausvuosi on " + str(muuttuja + 4))

    else:
        print("Vuotta " + str(vuosi) + " seuraava karkausvuosi on " + str(muuttuja))


if vuosi % 4 == 0:
    if (vuosi +4) % 400 == 0:
        print("Vuotta " + str(vuosi) + " seuraava karkausvuosi on " +str(vuosi+4))

    elif (vuosi +4) % 100 == 0:
        print("Vuotta " + str(vuosi) + " seuraava karkausvuosi on " + str(muuttuja+8))

    else:
        print("Vuotta " + str(vuosi) + " seuraava karkausvuosi on " + str(vuosi+4))

