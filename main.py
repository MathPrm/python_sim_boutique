from app.boutique import *

def main():

    # display a sentence using all variables
    print(f"Chez {nom_boutique}, nous vendons des {produit} au prix imbattable de {prix_unitaire} € et nous appliquons une tva exceptionnelle de {tva}, venez dépenser vos {compte_client} € pour remplir notre comptre qui aujourd'hui est à {compte_boutique} € avant que les {quantite_stock} dernières chaussettes ne disparaissent!")

    # let the user enter how much socks he would like to buy
    try:
        chaussettes_nombres = int(input("Veuillez entrer le nombre de chaussettes que vous souhaitez acheter : "))
    except ValueError:
        raise Exception("Veuillez rentrer un nombre entier et valide !")
    if chaussettes_nombres <= 0:
        raise Exception("Le nombre de chaussettes désirées ne peut être inférieur ou égal à 0 ! x(")
    if chaussettes_nombres > quantite_stock:
        raise Exception("La quantité de chaussettes souhaitées dépasse la limite des stocks diponibles, veuillez choisir un stock plus petit, ne vous en déplaise ! :D")

    facture()

# entry point
if __name__ == "__main__":
    main()