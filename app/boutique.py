# this file contains business logic that uses utilities to implement specific rules
from app.utils import *

# variables
chaussettes_nombre: int = 0
nom_boutique: str = "ChossettZ"
produit: str = "chaussettes"
prix_unitaire: float = 5.99
quantite_stock: int = 20
tva: float = 0.20
compte_client: int = 100
compte_boutique: int = 0

# calculate total price without taxes for socks desired
def montant_ht(quantite: int = None) -> float:
    # determine quantity of socks
    if quantite is None:
        quantite = chaussettes_nombre
    prix_ht = calcul_prix_ht(prix_unitaire, quantite)
    print(prix_ht)
    return prix_ht

# calculate total price with taxes for socks desired
def montant_ttc(prix_ht: float) -> float:
    prix_ttc = calcul_prix_ttc(prix_ht, tva)
    print(prix_ttc)
    return prix_ttc

# calculate total price tva for socks desired
def montant_tva(prix_ht: float, prix_ttc: float) -> float:
    prix_tva = prix_ttc - prix_ht
    return round(prix_tva, 2)

# display ttc price
def affichage_montant_ttc(prix_ttc: float) -> str:
   prix_ttc_affiche = affichage_prix(prix_ttc)
   print(prix_ttc_affiche)

# calculate number of socks still available in stocks after purchase
def quantite_stock_available(quantite: int = None) -> int:
     # determine quantity of socks
    if quantite is None:
        quantite = chaussettes_nombre
    stock = stock_encore_disponible(quantite, quantite_stock)
    print(stock)
    return stock

# debit client account
def debiter_compte_client(somme_debite: float) -> float:
    debit = debiter_compte(somme_debite, compte_client)
    boutique = crediter_compte(somme_debite, compte_boutique)
    print(f"Compte boutique : {boutique} € \n Compte client : {debit} €")
    return debit

# credit boutique account
def crediter_compte_boutique(somme_credite: float) -> float:
    credit = crediter_compte(somme_credite, compte_boutique)
    client = debiter_compte(somme_credite, compte_client)
    print(f"Compte boutique : {credit} € \n Compte client : {client} €")
    return credit

# stock soon to run out
def bientot_rupture_stock(quantite: int, prix: float) -> int:
    if 10 < quantite < 15 and prix > 5:
        print("!! Attention produit presque en ruptures !!")
    elif quantite > 10:
        print("!! Stock bientôt épuisé !!")
    return None

# display invoice
def facture(quantite: int = None) -> str:

    # determine quantity of socks
    if quantite is None:
        quantite = chaussettes_nombre

    # calculate prices with or without taxes and total pric payed for tva in function scope
    prix_ht = montant_ht(quantite)
    prix_ttc = montant_ttc(prix_ht)
    prix_tva = montant_tva(prix_ht, prix_ttc)

    print(f"{"":->80}")
    print(nom_boutique)
    print(f"{"":->80}")
    print(f"{"Produit": <20}{"qté": >40}{"ht": >20}")
    print(f"{"Chaussettes":.<40}{quantite: >20}{prix_ht: >20}")
    print(f"{"Total HT": >60}{prix_ht: >20}")
    print(f"{"TVA": >60}{prix_tva: >20}")
    print(f"{"Total TTC": >60}{prix_ttc: >20}")
    print(f"{"":->80}")
    