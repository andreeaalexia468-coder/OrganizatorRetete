
import json
from pathlib import Path
from clase import Ingredient, Pas, Reteta


CALE_FISIER = Path(__file__).resolve().parent / "retete.json"


def salveaza_retete(retete):
    CALE_FISIER.parent.mkdir(parents=True, exist_ok=True)

    lista_retete = []

    for reteta in retete:
        date_reteta = {
            "titlu": reteta.titlu,
            "ingrediente": [],
            "pasi": []
        }

        for ingredient in reteta.ingrediente:
            date_ingredient = {
                "nume": ingredient.nume,
                "cantitate": ingredient.cantitate,
                "unitate": ingredient.unitate
            }
            date_reteta["ingrediente"].append(date_ingredient)
        for pas in reteta.pasi:
            date_pas = {
                "ordine": pas.ordine,
                "descriere": pas.descriere,
                "ingrediente_folosite": pas.ingrediente_folosite
            }

            date_reteta["pasi"].append(date_pas)
            

        lista_retete.append(date_reteta)

    with open(CALE_FISIER, "w", encoding="utf-8") as fisier:
        json.dump(lista_retete, fisier, ensure_ascii=False, indent=4)


def incarca_retete():
    if not CALE_FISIER.exists():
        return []
    try:
        with open(CALE_FISIER, "r", encoding="utf-8") as fisier:
            lista_retete = json.load(fisier)
    except (json.JSONDecodeError, OSError):
        return []

    retete = []

    for date_reteta in lista_retete:
        ingrediente = []

        for date_ingredient in date_reteta["ingrediente"]:
            ingredient = Ingredient(
                date_ingredient["nume"],
                date_ingredient["cantitate"],
                date_ingredient["unitate"]
            )

            ingrediente.append(ingredient)
        pasi = []

        for date_pas in date_reteta["pasi"]:
            pas = Pas(
                date_pas["ordine"],
                date_pas["descriere"],
                date_pas["ingrediente_folosite"]
            )

            pasi.append(pas)
        
        reteta = Reteta(
            date_reteta["titlu"],
            ingrediente,
            pasi
        )

        retete.append(reteta)

    return retete
