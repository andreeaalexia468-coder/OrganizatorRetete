from clase import Ingredient, Pas, Reteta
from gestionare_retete import GestionareRetete
from salvare_date import salveaza_retete, incarca_retete

gestiune = GestionareRetete()
gestiune.retete = incarca_retete()

def adauga_reteta():
    print("\n--- ADAUGARE RETETA ---")

    titlu = input("Introdu titlul retetei: ")

    nr_ingrediente = int(input("Cate ingrediente are reteta? "))

    ingrediente = []

    for i in range(nr_ingrediente):
        print("\nIngredientul", i + 1)

        nume = input("Nume: ")
        cantitate = float(input("Cantitate: "))
        unitate = input("Unitate de masura: ")

        ingredient = Ingredient(nume, cantitate, unitate)
        ingrediente.append(ingredient)

    # Citim pasii de preparare
    nr_pasi = int(input("\nCati pasi de preparare are reteta? "))

    pasi = []

    for i in range(nr_pasi):
        print("\nPasul", i + 1)

        descriere = input("Descriere: ")

        nume_ingrediente = input(
            "Ingrediente folosite (separate prin virgula): "
        )

        ingrediente_folosite = []

        if nume_ingrediente.strip() != "":
            ingrediente_folosite = [
                nume.strip()
                for nume in nume_ingrediente.split(",")
            ]

        pas = Pas(i + 1, descriere, ingrediente_folosite)
        pasi.append(pas)

    try:
        reteta = Reteta(titlu, ingrediente, pasi)

        gestiune.adauga_reteta(reteta)
        salveaza_retete(gestiune.retete)

        print("\nReteta a fost adaugata si salvata cu succes!")

    except ValueError as eroare:
        print("\nEroare:", eroare)


def afiseaza_retete():
    retete = gestiune.afiseaza_retete()

    if not retete:
        print("\nNu exista retete salvate.")
        return

    for reteta in retete:
        print("\nReteta:", reteta.titlu)

        print("Ingrediente:")
        for ingredient in reteta.ingrediente:
            print(
                ingredient.nume,
                ingredient.cantitate,
                ingredient.unitate
            )

        print("Pasi de preparare:")
        for pas in reteta.pasi:
            print(pas.ordine, "-", pas.descriere)

def cauta_reteta():
    nume_ingredient = input("\nIntrodu ingredientul cautat: ")

    retete_gasite = gestiune.cauta_dupa_ingredient(nume_ingredient)

    if not retete_gasite:
        print("\nNu exista retete care contin acest ingredient.")
        return

    print("\nRetete care contin", nume_ingredient, ":")

    for reteta in retete_gasite:
        print("-", reteta.titlu)


#meniu principal
while True:
    print("\n===== ORGANIZATOR DE RETETE =====")
    print("1. Adauga reteta")
    print("2. Afiseaza retetele")
    print("3. Cauta dupa ingredient")
    print("4. Iesire")

    optiune = input("\nAlege o optiune: ")

    if optiune == "1":
        adauga_reteta()

    elif optiune == "2":
        afiseaza_retete()

    elif optiune == "3":
        cauta_reteta()

    elif optiune == "4":
        print("La revedere!")
        break

    else:
        print("Optiune invalida!")



