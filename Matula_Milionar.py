import csv
import matplotlib.pyplot as plt
import random

Prihlasene_Jmeno = None
Prihlasene_Heslo = None

def Menu1():
    global Prihlasene_Jmeno
    global Prihlasene_Heslo
    while True:
        print("1) Založení účtu")
        print("2) Přihlášení")
        print("3) Konec")
        Vyber = input()
        if Vyber == "1":
            Zalozeni_uctu()
        elif Vyber == "2":
            Jmeno, Heslo = Prihlaseni()
            if Jmeno is not None:
                Prihlasene_Jmeno = Jmeno
                Prihlasene_Heslo = Heslo
                Menu2()
        elif Vyber == "3":
            quit()

def Zalozeni_uctu():
    with open("soubory/udaje.csv", "a", encoding="utf-8") as file:
        print("Založ si účet")
        Jmeno = input("Zadej jméno: ")
        Heslo = input("Zadej heslo: ")
        Udaj = f'{Jmeno},{Heslo}'
        file.write(f'{Udaj}\n')

def Prihlaseni():
    while True:
        with open("soubory/udaje.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            print("Přihlaš se")
            Jmeno = input("Zadej jméno: ")
            Heslo = input("Zadej heslo: ")
            for line in reader:
                if line[0] == Jmeno and line[1] == Heslo:
                    return Jmeno, Heslo
            print("Špatné údaje, zkus to znovu")
            return None, None

def Menu2():
    while True:
        print("1) Hra")
        print("2) Vítězové")
        print("3) Grafy")
        print("4) Konec")
        Vyber2 = input()
        if Vyber2 == "1":
            Hra()
        elif Vyber2 == "2":
            Vitezove()
        elif Vyber2 == "3":
            Vyber_grafu()
        elif Vyber2 == "4":
            quit()

def Hra():
    Pocet_spravnych_odpovedi = 0
    Jmeno = Prihlasene_Jmeno
    Heslo = Prihlasene_Heslo
    Jednoduche_otazky = []
    Stredni_otazky = []
    Tezke_otazky = []
    with open("2. prace_se_soubory/PROJEKT_milionar/quiz_questions.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for line in reader:
            if line[1] == "easy":
                Jednoduche_otazky.append({"Otázka": line[3], "Odpověď": line[4]})
            elif line[1] == "medium":
                Stredni_otazky.append({"Otázka": line[3], "Odpověď": line[4]})
            elif line[1] == "hard":
                Tezke_otazky.append({"Otázka": line[3], "Odpověď": line[4]})
        for i in range(5):    
            Kolo = random.choice(Jednoduche_otazky)
            print(i+1, "kolo")
            print(Kolo["Otázka"])
            print(Kolo["Odpověď"])
            Odpoved_hrace = input()
            if Kolo["Odpověď"] == "True":
                if Odpoved_hrace == "True":
                    print("Správná odpověď")
                    Pocet_spravnych_odpovedi += 1
                else:
                    print("Špatná odpověď")
            else:
                if Odpoved_hrace == "False":
                    print("Správná odpověď")
                    Pocet_spravnych_odpovedi += 1
                else:
                    print("Špatná odpověď")

        for i in range(5):    
            Kolo = random.choice(Stredni_otazky)
            print(i+6, "kolo")
            print(Kolo["Otázka"])
            print(Kolo["Odpověď"])
            Odpoved_hrace = input()
            if Kolo["Odpověď"] == "True":
                if Odpoved_hrace == "True":
                    print("Správná odpověď")
                    Pocet_spravnych_odpovedi += 1
                else:
                    print("Špatná odpověď")
            else:
                if Odpoved_hrace == "False":
                    print("Správná odpověď")
                    Pocet_spravnych_odpovedi += 1
                else:
                    print("Špatná odpověď")
        for i in range(5):
            Kolo = random.choice(Tezke_otazky)
            print(i+11, "kolo")
            print(Kolo["Otázka"])
            print(Kolo["Odpověď"])
            Odpoved_hrace = input()
            if Kolo["Odpověď"] == "True":
                if Odpoved_hrace == "True":
                    print("Správná odpověď")
                    Pocet_spravnych_odpovedi += 1
                else:
                    print("Špatná odpověď")
            else:
                if Odpoved_hrace == "False":
                    print("Správná odpověď")
                    Pocet_spravnych_odpovedi += 1
                else:
                    print("Špatná odpověď")
        print("Počet správných odpovědí:", Pocet_spravnych_odpovedi)
        Zprava = input("Vyhrál jsi, napiš zprávu: ")
        with open("soubory/vitezove.csv", "a", encoding="utf-8") as file:
            Udaj = f'{Jmeno},{Heslo},{Zprava}'
            file.write(f"{Udaj}\n")
                    
def Vitezove():
    with open("soubory/vitezove.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        print("Seznam vítězů")
        for line in reader:
            print(line[0], line[1], line[2])

def Vyber_grafu():
    while True:
        print("1) Obtížnosti")
        print("2) Kategorie")
        print("3) Konec")
        Vyber3 = input()
        if Vyber3 == "1":
            Obtiznosti()
        elif Vyber3 == "2":
            Kategorie()
        elif Vyber3 == "3":
            quit()

def Obtiznosti():
    with open("2. prace_se_soubory/PROJEKT_milionar/quiz_questions.csv", "r", encoding="utf-8") as file:
        Obtiznosti_pole = []
        Pocet_otazek = 0
        Pocet_jednoduchych_otazek = 0
        Pocet_strednich_otazek = 0
        Pocet_tezkych_otazek = 0
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if line[1] not in Obtiznosti_pole:
                Obtiznosti_pole.append(line[1])
            if line[1] == "easy":
                Pocet_jednoduchych_otazek += 1
                Pocet_otazek += 1
            elif line[1] == "medium":
                Pocet_strednich_otazek += 1
                Pocet_otazek += 1
            elif line[1] == "hard":
                Pocet_tezkych_otazek += 1
                Pocet_otazek += 1
        plt.bar(Obtiznosti_pole, [Pocet_jednoduchych_otazek, Pocet_strednich_otazek, Pocet_tezkych_otazek])
        plt.title("Poměr obtížností v datasetu otázek")
        plt.ylabel("Počet otázek")
        plt.xticks(rotation=45, ha="right")
        print("pocet jednoduchych otazek: ", Pocet_jednoduchych_otazek)
        print("pocet strednich otazek: ", Pocet_strednich_otazek)
        print("pocet tezkych otazek: ", Pocet_tezkych_otazek)
        print("Počet otázek:", Pocet_otazek)
        plt.show()

def Kategorie():
    with open("2. prace_se_soubory/PROJEKT_milionar/quiz_questions.csv", "r", encoding="utf-8") as file:
        general_knowledge = 0
        books = 0
        film = 0
        music = 0
        video_games = 0
        nature = 0
        computers = 0
        geography = 0
        history = 0
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if line[2] == "General Knowledge":
                general_knowledge += 1
            elif line[2] == "Entertainment: Books":          
                books += 1
            elif line[2] == "Entertainment: Film":          
                film += 1
            elif line[2] == "Entertainment: Music":          
                music += 1
            elif line[2] == "Entertainment: Video Games":           
                video_games += 1
            elif line[2] == "Science: Nature":      
                nature += 1
            elif line[2] == "Science: Computers":      
                computers += 1
            elif line[2] == "Geography":
                geography += 1
            elif line[2] == "History":
                history += 1
            
            Kategorie = ["General Knowledge", "Entertaiment: Books", "Entertaiment: Film", "Entertaiment: Music", "Entertaiment: Video Games", "Science: Nature", "Science: Computers", "Geography", "History"]
            Pocet_kategorii = [general_knowledge, books, film, music, video_games, nature, computers, geography, history]
        plt.bar(Kategorie, Pocet_kategorii)
        plt.title("Poměr kategorií v datasetu otázek")
        plt.ylabel("Počet otázek")
        plt.xticks(rotation=45, ha="right")
        print("pocet otazek v General Knowledge:", general_knowledge)
        print("pocet otazek v Entertainment: Books:", books)
        print("pocet otazek v Entertainment: Film:", film)
        print("pocet otazek v Entertainment: Music:", music)
        print("pocet otazek v Entertainment: Video Games:", video_games)
        print("pocet otazek v Science: Nature:", nature)
        print("pocet otazek v Science: Computers:", computers)
        print("pocet otazek v Geography:", geography)
        print("pocet otazek v History:", history)
        plt.show()

Menu1()