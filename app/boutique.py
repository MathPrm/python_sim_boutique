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
def montant_ht() -> float:
    quantite = chaussettes_nombre
    prix_ht = calcul_prix_ht(prix_unitaire, quantite)
    return prix_ht

# calculate total price with taxes for socks desired
def montant_ttc() -> float:
    prix_ht = montant_ht()
    prix_ttc = calcul_prix_ttc(prix_ht, tva)
    return prix_ttc

# calculate total price tva for socks desired
def montant_tva() -> float:
    prix_tva = montant_ttc() - montant_ht()
    return prix_tva

# display ttc price
def affichage_montant_ttc() -> str:
   prix_ttc = montant_ttc()
   prix_ttc_affiche = affichage_prix(prix_ttc)
   print(prix_ttc_affiche)

# calculate number of socks still available in stocks after purchase
def quantite_stock_available() -> int:
    quantite = chaussettes_nombre
    stock = stock_encore_disponible(quantite, quantite_stock)
    return stock

# debit client account
def debiter_compte_client() -> float:
    somme_debite = montant_ttc()
    return debiter_compte(somme_debite, compte_client)

# credit boutique account
def crediter_compte_boutique() -> float:
    somme_credite = montant_ttc()
    return crediter_compte(somme_credite, compte_boutique)

# stock soon to run out
def bientot_rupture_stock() -> int:
    if quantite_stock_available() < 10:
        return print("!! Stock bientôt épuisé !!")
    elif 10 <quantite_stock_available() < 15 and prix_unitaire > 5:
        print("!! Attention produit presque en ruptures !!")
    return None

# display invoice
def facture() -> str:
    prix_ht = montant_ht()
    prix_ttc = montant_ttc()
    prix_tva = montant_tva()
    print(f"{"":->80}")
    print(nom_boutique)
    print(f"{"":->80}")
    print(f"{"Produit": <20}{"qté": >40}{"ht": >20}")
    print(f"{"Chaussettes":.<40}{chaussettes_nombre: >20}{prix_ht: >20}")
    print(f"{"Total HT": >60}{prix_ht: >20}")
    print(f"{"TVA": >60}{prix_tva: >20}")
    print(f"{"Total TTC": >60}{prix_ttc: >20}")
    print(f"{"":->80}")
    