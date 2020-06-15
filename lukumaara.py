print("Syötä kokonaislukuja, 0 lopettaa:")
luku = int(input("Luku: "))

lkm = 0
positiiviset = 0
negatiiviset = 0

if luku > 0:
    positiiviset = positiiviset + 1

if luku < 0:
    negatiiviset = negatiiviset + 1

summa = luku

while luku != 0:
    luku = int(input("Luku: "))
    summa = summa + luku
    lkm = lkm + 1

    if luku > 0:
        positiiviset = positiiviset +1

    if luku < 0:
        negatiiviset = negatiiviset + 1

print("Lukuja yhteensä " +str(lkm))
print("lukujen summa " +str(summa))
print("lukujen keskiarvo " +str(summa/lkm))
print("Positiivisia: " +str(positiiviset))
print("Negatiivisia: " +str(negatiiviset))


