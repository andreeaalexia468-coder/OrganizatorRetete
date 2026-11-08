from clase import Ingredient, Reteta // #importam clasele definite in primul fisier, ca sa folosim aici

class GestionareRetete:
    def __init__(self):
        self.retete = []  #self.retete este lista in care pastram toate retetele, initial fiind goala []

    def adauga_reteta(self, reteta):
      self.retete.append(reteta)   #primim o reteta si se adauga in lista prin append()
