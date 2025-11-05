# this file contains business logic that uses utilities to implement specific rules
from app.utils import (
    calcul_prix_ht,
    calcul_prix_ttc,
    stock_encore_disponible,
    crediter_compte,
    debiter_compte
)

# variables
nom_boutique: str = "ChossettZ"
produit: str = "chaussettes"
prix_unitaire: float = 5.99
quantite_stock: int = 20
tva: float = 0.20
compte_client: int = 100
compte_boutique: int = 0

# let the user enter how much socks he would like to buy
def combien_de_chaussettes() -> int:
    try:
        chaussettes_nombres = int(input("Veuillez entrer le nombre de chaussettes que vous souhaitez acheter : "))
    except ValueError:
        raise Exception("Veuillez rentrer un nombre entier et valide !")
    if chaussettes_nombres <= 0:
        raise Exception("Le nombre de chaussettes désirées ne peut être inférieur ou égal à 0 ! x(")
    if chaussettes_nombres > quantite_stock:
        raise Exception("La quantité de chaussettes souhaitées dépasse la limite des stocks diponibles, veuillez choisir un stock plus petit, ne vous en déplaise ! :D")
    return chaussettes_nombres

# calculate total price without taxes for socks desired
def montant_ht() -> float:
    quantite = combien_de_chaussettes()
    prix_ht = calcul_prix_ht(prix_unitaire, quantite)
    return prix_ht

# calculate total price with taxes for socks desired
def montant_ttc() -> float:
    prix_ht = montant_ht()
    prix_ttc = calcul_prix_ttc(prix_ht, tva)
    return prix_ttc

# calculate number of socks still available in stocks after purchase
def quantite_stock_available() -> int:
    quantite = combien_de_chaussettes()
    stock = stock_encore_disponible(quantite, quantite_stock)
    return stock

# debit client account
def debiter_compte_client() -> float:
    somme_debite = montant_ttc
    return debiter_compte(somme_debite, compte_client)

# credit boutique account
def crediter_compte_boutique() -> float:
    somme_credite = montant_ttc
    return crediter_compte(somme_credite, compte_boutique)

# stock soon to run out
def bientot_rupture_stock() -> int:
    if quantite_stock_available < 10:
        return print("!! Stock bienôt épuisé !!")
    elif 10 <quantite_stock_available() < 15 and prix_unitaire > 5:
        print("!! Attention produit presque en ruptures !!")
    return None