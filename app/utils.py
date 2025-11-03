# this file contains generic mathematical and formatting function

# calculation of total price excluding tax
def calcul_prix_ht(prix_unitaire: float, quantite: int) -> float:
    prix_ht = prix_unitaire * quantite
    return round(prix_ht, 2)

# calculation of the total price including all taxes
def calcul_prix_ttc(prix_ht: float, tva: float) -> float:
    prix_ttc = prix_ht * (1 + tva)
    return round(prix_ttc, 2)