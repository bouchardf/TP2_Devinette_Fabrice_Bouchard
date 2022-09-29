from random import*

nb_essai = 0
fin_jeu = False
rejouer = None


print("J’ai choisi un nombre au hasard entre 0 et 1000. "
      "À vous de le deviner...")

nombre_aleatoire = randint(0, 1000)

while fin_jeu == False:
    nb_joueur = int(input("Entrez votre essai :_"))
    nb_essai = nb_essai + 1

    if nb_joueur > nombre_aleatoire:
        print("Mauvais choix, le nombre est plus petit que" ,nb_joueur,)


    elif nb_joueur < nombre_aleatoire:
        print("Mauvaise réponse, le nombre est plus grand que" ,nb_joueur,)

    elif nb_joueur == nombre_aleatoire:
        print("Bravo! Bonne réponse! Vous avez réussi en:", nb_essai, "essais")

        rejouer = input("Voulez rejouer? Entrer n pour quitter et o pour continuer.")

        if rejouer == "n":
            print("Merci et au revoir...")
            fin_jeu = True

        elif rejouer == "o":
            nb_essai = 0
            nombre_aleatoire = randint(0, 1000)