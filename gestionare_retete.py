
from clase import Ingredient, Reteta


class GestionareRetete:
    def __init__(self):
        self.retete = []

    def adauga_reteta(self, reteta):
        self.retete.append(reteta)

    def afiseaza_retete(self):
        return self.retete

    def cauta_dupa_ingredient(self, nume_ingredient):
        retete_gasite = []

        for reteta in self.retete:
            for ingredient in reteta.ingrediente:
                if ingredient.nume.lower() == nume_ingredient.lower():
                    retete_gasite.append(reteta)
                    break

        return retete_gasite
