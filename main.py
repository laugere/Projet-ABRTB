import random
import os

import main
import noeud
import functions


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def InitMenu():
    choix = 999
    if (mainABRTB == None):
        while int(choix) not in [0, 1, 2]:
            print("1 - Fichier vers ABRTB")
            print("2 - ABRTB aléatoire")
            print("0 - Sortir")
            choix = input("Choix : ")
    else:
        while int(choix) not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            print("Generate and save")
            print("1 - ABRTB vers fichier")
            print("2 - Affichage à l'écran")
            print("3 - Vérification")
            print("Manipulate")
            print("4 - Recherche d'un entier")
            print("5 - Suppression d'un entier")
            print("6 - Insertion d'un entier")
            print("7 - ABRTB vers ABR")
            print("8 - ABRTB vers ABR des k-ièmes plus grands éléments")
            print("0 - Sortir")
            choix = input("Choix : ")
    return choix


def ActionSelect(index):
    global mainABRTB
    # Create ABRTB from file
    if index == 0:
        path = input(
            "Indiquez le lien vers le fichier ABRTB (Entrée pour le fichier par défaut) : ")
        mainABRTB = functions.CreateABRTBFromFile(path)
        print("Fichier importé")
        input("\nEntrer pour passer")
    # Export ABRTB to file
    elif index == 1:
        path = input(
            "Indiquez le lien vers le fichier ABRTB (Entrée pour le fichier par défaut) : ")
        functions.ExportABRTBToFile(mainABRTB, path)
        print("Fichier exporté")
        input("\nEntrer pour passer")
    # Display ABRTB
    elif index == 2:
        functions.DisplayABRTB(mainABRTB)
        input("\nEntrer pour passer")
    # Create Random ABRTB
    elif index == 3:
        p = int(input("Nombre de noeuds pour l'ABRTB : "))
        q = int(input("Valeure maximum : "))
        mainABRTB = functions.RandomABRTB(p, q)
    # Verify ABRTB
    elif index == 4:
        print(functions.VerifABRTB(mainABRTB))
        input("\nEntrer pour passer")
    # Search value
    elif index == 5:
        value = int(input("Entrez la valeur à chercher : "))
        functions.SearchInteger(mainABRTB, value)
        input("\nEntrer pour passer")
    # Delete value
    elif index == 6:
        value = int(input("Entrez la valeur à supprimer : "))
        functions.DeleteInteger(mainABRTB, value)
        input("\nEntrer pour passer")
    # Insert value
    elif index == 7:
        value = int(input("Entrez la valeur à insérer : "))
        functions.InsertInteger(mainABRTB, value)
        input("\nEntrer pour passer")
    # ABRTB To ABR
    elif index == 8:
        functions.ABRTBToABR()
        input("\nEntrer pour passer")
    # ABRTB To ABR kieme
    elif index == 9:
        functions.ABRTBToABRkieme()
        input("\nEntrer pour passer")
    cls()


if __name__ == "__main__":
    global mainABRTB
    mainABRTB = None
    choix = 999
    cls()

    while(int(choix) not in [0]):
        choix = InitMenu()
        cls()
        if (mainABRTB == None):
            # Create ABRTB from file
            if int(choix) == 1:
                ActionSelect(0)
            # Create Random ABRTB
            elif int(choix) == 2:
                ActionSelect(3)
        else:
            # Export ABRTB to file
            if int(choix) == 1:
                ActionSelect(1)
            # Display ABRTB
            elif int(choix) == 2:
                ActionSelect(2)
            # Verify ABRTB
            elif int(choix) == 3:
                ActionSelect(4)
            # Search value
            elif int(choix) == 4:
                ActionSelect(5)
            # Delete value
            elif int(choix) == 5:
                ActionSelect(6)
            # Insert value
            elif int(choix) == 6:
                ActionSelect(7)
            # ABRTB to ABR
            elif int(choix) == 7:
                ActionSelect(8)
            # ABRTB to ABR kiemes
            elif int(choix) == 8:
                ActionSelect(9)

    print("GoodBye")
