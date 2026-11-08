class Ingredient:
  def __init__(self, nume, cantitate, unitate):
      self.nume = nume
      self.cantitate = cantitate
      self.unitate = unitate

class Reteta:
  def __init__(self, titlu, ingrediente, pasi):
      self.titlu = titlu
      self.ingrediente = ingrediente
      self.pasi = pasi
