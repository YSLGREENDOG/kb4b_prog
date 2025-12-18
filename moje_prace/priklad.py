import random

def generuj_priklad(radek):
    cislo1 = int(radek.split()[0])
    op = radek.split()[1]
    cislo2 = int(radek.split()[2])

    vstup = int(input((f"{cislo1} {op} {cislo2} = ")))

    if op == "+":
        spravne = cislo1 + cislo2
    elif op == "-":
        spravne = cislo1 - cislo2
    elif op == "*":
        spravne = cislo1 * cislo2

    return vstup == spravne

cesta = "2. prace_se_soubory/data/priklady.txt"

with open(cesta, "r", encoding="utf-8") as file:

    spravne = 0
   
    for line in file.readlines():
       # print(line)
        if generuj_priklad(line.strip()) == True:
            spravne += 1

print("Spravne: ", spravne, end="")



