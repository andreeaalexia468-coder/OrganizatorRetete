from clase import Ingredient, Reteta
from gestionare_retete import GestionareRetete

gestiune = GestionareRetete() #am creat obiectul care gestioneaza retetele

faina = Ingredient("Faina", 200, "grame")
lapte = Ingredient("Lapte", 500, "ml")
oua = Ingredient("Oua", 2, "bucati")

ingrediente_clatite = [faina, lapte, oua]
clatite = Reteta("Clatite", ingrediente_clatite, ["Amestecam ingredientele", "Coacem clatitele"])

gestiune.adauga_reteta(clatite)

for reteta in gestiune.afiseaza_retete():
    print("Reteta:", reteta.titlu)
    print("Ingrediente:")
    for ingredient in reteta.ingrediente:
      print(ingredient.nume, ingredient.cantitate, ingredient.unitate)
    print("Pasi de preparare:")
    for pas in reteta.pasi:
      print("-", pas)
