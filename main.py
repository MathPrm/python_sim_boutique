from app.boutique import (
    nom_boutique,
    produit,
    prix_unitaire,
    tva,
    compte_client,
    compte_boutique,
    quantite_stock,
    combien_de_chaussettes,
    montant_ht,
    montant_ttc,
    quantite_stock_available
)

def main():

    # display a sentence using all variables
    print(f"Chez {nom_boutique}, nous vendons des {produit} au prix imbattable de {prix_unitaire} € et nous appliquons une tva exceptionnelle de {tva}, venez dépenser vos {compte_client} € pour remplir notre comptre qui aujourd'hui est à {compte_boutique} € avant que les {quantite_stock} dernières chaussettes ne disparaissent!")

    quantite_stock_available()

# entry point
if __name__ == "__main__":
    main()