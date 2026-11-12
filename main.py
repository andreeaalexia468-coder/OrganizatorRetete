from clase import Ingredient, Pas, Reteta
from gestionare_retete import GestionareRetete
from salvare_date import salveaza_retete, incarca_retete

gestiune = GestionareRetete() #am creat obiectul care gestioneaza retetele
gestiune.retete = incarca_retete()

faina = Ingredient("Faina", 200, "grame")
lapte = Ingredient("Lapte", 500, "ml")
oua = Ingredient("Oua", 2, "bucati")

ingrediente_clatite = [faina, lapte, oua]
pas1 = Pas(1,"Amestecam ingredientele", ["Faina", "Lapte", "Oua"])

pas2 = Pas(2,"Lasam aluatul sa se odihneasca",[])

pas3 = Pas(3,"Coacem clatitele",[])

pasi_clatite = [pas1, pas2, pas3]

clatite = Reteta("Clatite",ingrediente_clatite,pasi_clatite)

if not gestiune.retete:
    gestiune.adauga_reteta(clatite)

salveaza_retete(gestiune.retete)

for reteta in gestiune.afiseaza_retete():
    print("Reteta:", reteta.titlu)
    print("Ingrediente:")
    for ingredient in reteta.ingrediente:
      print(ingredient.nume, ingredient.cantitate, ingredient.unitate)
    print("Pasi de preparare:")
    for pas in reteta.pasi:
      print(pas.ordine, "-", pas.descriere)
