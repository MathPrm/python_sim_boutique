from app.boutique import (
    nom_boutique,
    produit,
    prix_unitaire,
    tva,
    compte_client,
    compte_boutique,
    quantite_stock,
)

def main():

    # display a sentence using all variables
    print(f"Chez {nom_boutique}, nous vendons des {produit} au prix imbattable de {prix_unitaire} € et nous appliquons une tva exceptionnelle de {tva}, venez vite rejoindre nos {compte_client} comptes clients auprès de nos {compte_boutique} comptes boutique avant que les {quantite_stock} dernières chaussettes ne disparaissent!")

# entry point
if __name__ == "__main__":
    main()