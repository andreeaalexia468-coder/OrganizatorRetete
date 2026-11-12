class Ingredient:
  def __init__(self, nume, cantitate, unitate):
      if cantitate <= 0:
            raise ValueError("Cantitatea trebuie sa fie pozitiva!")
      self.nume = nume
      self.cantitate = cantitate
      self.unitate = unitate

class Pas:
    def __init__(self, ordine, descriere, ingrediente_folosite):
        if ordine <= 0:
            raise ValueError("Numarul pasului trebuie sa fie pozitiv!")

        self.ordine = ordine
        self.descriere = descriere
        self.ingrediente_folosite = ingrediente_folosite

    def verifica_ingrediente(self, ingrediente_reteta):
        for ingredient_folosit in self.ingrediente_folosite:
            exista = False

            for ingredient in ingrediente_reteta:
                if ingredient_folosit.lower() == ingredient.nume.lower():
                    exista = True
                    break

            if not exista:
                raise ValueError(
                    f"Ingredientul {ingredient_folosit} nu exista in reteta!"
                )

        return True

class Reteta:
  def __init__(self, titlu, ingrediente, pasi):
      self.titlu = titlu
      self.ingrediente = ingrediente
      self.pasi = pasi

      for pas in self.pasi:
        pas.verifica_ingrediente(self.ingrediente)

