#Jeu de devinette
#29 septembre 2022
#Créé par Fabrice Bouchard

from random import*

#Défnition des variables

nb_essai = 0
fin_jeu = False
rejouer = None

borneUn = int(input("Entrez la première borne:"))

borneDeux = int(input("Entrez la deuxième borne:"))

nombre_aleatoire = randint(borneUn, borneDeux)

print("J’ai choisi un nombre au hasard entre", borneUn,"et" ,borneDeux,". À vous de le deviner...")


#Mise en place de la boucle dans laquelle le jeu prend place
while fin_jeu == False:
    nb_joueur = int(input("Entrez votre essai :_"))
    nb_essai = nb_essai + 1

    if nb_joueur > nombre_aleatoire:        #Si le nombre est plus petit
        print("Mauvais choix, le nombre est plus petit que" ,nb_joueur,)


    elif nb_joueur < nombre_aleatoire:      #Si le nombre est plus grand
        print("Mauvaise réponse, le nombre est plus grand que" ,nb_joueur,)

    elif nb_joueur == nombre_aleatoire:     #Si l'essai est le bon
        print("Bravo! Bonne réponse! Vous avez réussi en:", nb_essai, "essais")

        rejouer = input("Voulez rejouer? Entrer n pour quitter et o pour continuer.")

        if rejouer == "n":      #Si le joueur veut quitter
            print("Merci et au revoir...")
            fin_jeu = True

        elif rejouer == "o":       #Si le joueur veut rejouer
            nb_essai = 0
            borneUn = int(input("Entrez la première borne:"))
            borneDeux = int(input("Entrez la deuxième borne:"))
            nombre_aleatoire = randint(borneUn, borneDeux)
            print("J’ai choisi un nombre au hasard entre", borneUn, "et", borneDeux, ". À vous de le deviner...")
