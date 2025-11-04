# this file contains business logic that uses utilities to implement specific rules

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
    return print(f"Vous souhaitez acheter {chaussettes_nombres} chaussetZ ! Excellent choix!")