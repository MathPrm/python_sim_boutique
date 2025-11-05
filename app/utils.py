# this file contains generic mathematical and formatting function

# calculation of total price excluding tax
def calcul_prix_ht(prix_unitaire: float, quantite: int) -> float:
    prix_ht = prix_unitaire * quantite
    return round(prix_ht, 2)

# calculation of the total price including all taxes
def calcul_prix_ttc(prix_ht: float, tva: float) -> float:
    prix_ttc = prix_ht * (1 + tva)
    return round(prix_ttc, 2)

# calculation of the the stock still available after purchase
def stock_encore_disponible(quantite_achetee: int, quantite_stock: int) -> int:
    return quantite_stock - quantite_achetee

# credit an account
def crediter_compte(somme_credite: float, compte_credite: float) -> float:
    return compte_credite + somme_credite

# debit an account
def debiter_compte(somme_debite: float, compte_debite: float) -> float:
    return compte_debite - somme_debite

# price to type string
def affichage_prix(number: float) -> str:
    prix_str = str(number)
    return f"{prix_str} €"