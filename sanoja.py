sana = input("Anna sana: ")
teksti =""
vanha =""

while sana != "loppu":
    vanha = sana
    teksti = teksti + sana +" "
    sana = input("Anna sana: ")
    if sana == vanha:
        break

print(teksti)