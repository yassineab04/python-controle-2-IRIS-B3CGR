import random
from datetime import datetime
import csv
carnet_parties = [] 
def partie():
    print("\n--- NOUVELLE PARTIE ---")
    print("\nAppuyez sur '0' pour annuler et revenir au menu.")
    date_du_tour = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    options = ["pierre", "feuille", "ciseau"]
    
    choix_joueur_index = input("\nVOTRE CHOIX (1.pierre, 2.feuille, 3.ciseau) : ")


    if choix_joueur_index == "0":
        print("Partie annulée.")
        return

    if choix_joueur_index not in ["1", "2", "3"]:
        print("ERREUR : Choix invalide !")
        return
        

    choix_joueur = options[int(choix_joueur_index) - 1]
    choix_cpu = random.choice(options)
    
    
    if choix_joueur == choix_cpu:
        res = "Nul"
    elif (choix_joueur == "pierre" and choix_cpu == "ciseau") or \
         (choix_joueur == "feuille" and choix_cpu == "pierre") or \
         (choix_joueur == "ciseau" and choix_cpu == "feuille"):
        res = "Gagné"
    else:
        res = "Perdu"

    print(f"> Tu as choisi : {choix_joueur}")
    print(f"> Le CPU a choisi : {choix_cpu}")
    print(f"J: {choix_joueur} | CPU: {choix_cpu} -> {res}")

    ligne_a_sauver = [date_du_tour, choix_joueur, choix_cpu, res]
    carnet_parties.append([date_du_tour,choix_joueur, choix_cpu, res])


    try:
        with open("historique_jeu.csv", mode="a", encoding="utf-8", newline="") as fichier:
            writer = csv.writer(fichier)
            writer.writerow(ligne_a_sauver)   
    except IOError as e:
        print(f"Impossible de sauvegarder : {e}")

def afficher_historique():
    print("\n--- HISTORIQUE DES PARTIES ---")
    if len(carnet_parties) == 0 :
            print("aucune historique n'est generer")
    else:
        try:
            with open("historique_jeu.csv", mode="r", encoding="utf-8") as fichier:
                lecteur = csv.DictReader(fichier, fieldnames=["Date", "Joueur", "CPU", "Resultat"])
            
                for ligne in lecteur:
                    print(f"[{ligne['Date']}] J: {ligne['Joueur']} -> {ligne['Resultat']}")
                    
        except FileNotFoundError:
                    print("⚠️ Erreur : Le fichier 'historique_jeu.csv' n'existe pas encore.")
        except Exception as e:
                    print(f"⚠️ Une erreur est survenue : {e}")



def afficher_statistique():
    print("\n--- TABLEAU DE BORD ---")

    total=0
    victoires=0
    mains_gagnantes = {"pierre": 0, "feuille": 0, "ciseau": 0}

    try:
         with open("historique_jeu.csv", mode="r", encoding="utf-8") as fichier:
              lecteur =csv.DictReader(fichier,fieldnames=["Date", "Joueur", "CPU", "Resultat"])

              for ligne in lecteur:
                   total += 1

                   if ligne["Resultat"]=="Gagné":
                        victoires += 1
                        main_utilisee = ligne["Joueur"]
                        if main_utilisee in mains_gagnantes:
                             mains_gagnantes[main_utilisee] += 1
         if total > 0:
            taux = (victoires / total) * 100
            print(f"📊 Parties jouées : {total}")
            print(f"🏆 Victoires : {victoires} ({taux:.1f}%)")
            print("\n🔥 Tes meilleures mains :")
            for main, nbre in mains_gagnantes.items():
                print(f"   - {main.capitalize()} : {nbre} fois")
         else:
            print("Jouez au moins une partie pour voir vos stats !")    

    except FileNotFoundError:
        print("⚠️ Pas encore de fichier d'historique.")

def main():
    while True:
     print("\nMENU")
     print("1. Commencer une nouvelle partie")
     print("2. Consulter l'historique")
     print("3. Consulter l'estatistiques")
     print("4. Quitter le jeu")

     choix = input("VOTRE CHOIX : ")

     if choix == "4":
        print("Au revoir !")
        break
     elif choix == "1":
        while True:
            partie()

            while True:
                rejouer = input("\n Rejouer(o),retourner au menu principaln(n):").lower()
                if rejouer == 'o':
                    break
                elif rejouer == 'n':
                    break
                else:
                    print("S'il vous plaît, répondez par 'o' ou 'n'.")
            if rejouer == 'n':
                break   
     elif choix == "2":
                afficher_historique()
                input("\nAppuyez sur Entrée pour retourner au menu principal...")
     elif choix == "3":
        while True:
                afficher_statistique()
                input("\nAppuyez sur Entrée pour retourner au menu principal...")
                break

if __name__ == "__main__":
    main()