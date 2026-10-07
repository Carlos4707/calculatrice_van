def calculer_van():
    print("--- SIMULATEUR DE PROJET D'INVESTISSEMENT (VAN) ---")
    
    try:
        # 1. Récupération des données initiales
        investissement = float(input("Entrez l'investissement initial (ex: 10000) : "))
        taux = float(input("Entrez le taux d'actualisation en % (ex: 10 pour 10%) : ")) / 100
        annees = int(input("Entrez la durée du projet en années (ex: 3) : "))
        
        somme_cash_flows_actualises = 0
        
        # 2. Boucle dynamique pour collecter et actualiser les Cash-Flows
        for annee in range(1, annees + 1):
            cf = float(input(f"Entrez le Cash-Flow pour l'année {annee} : "))
            
            # Application de la formule financière : CF / (1 + t)^annee🏝
            cf_actualise = cf / ((1 + taux) ** annee)
            somme_cash_flows_actualises += cf_actualise
            
        # 3. Calcul final de la VAN
        van = somme_cash_flows_actualises - investissement
        
        # 4. Affichage du verdict financier
        print("\n---------------- RESULTAT ----------------")
        print(f"La Valeur Actuelle Nette (VAN) est de : {van:.2f} $")
        
        if van > 0:
            print("Verdict : Le projet est RENTABLE ! Vous pouvez investir. ✅")
        elif van == 0:
            print("Verdict : Le projet atteint juste l'équilibre. ⚖️")
        else:
            print("Verdict : Le projet n'est PAS RENTABLE. À rejeter ! ❌")
            
    except ValueError:
        print("Erreur : Veuillez entrer des chiffres valides.")

# Lancement du programme
if __name__ == "__main__":
    calculer_van()

