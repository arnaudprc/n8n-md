# Exemple de programme Python avec commentaires basiques

# On definit une fonction qui calcule la somme de deux nombres
def addition(a, b):
    # On retourne le resultat de l'addition
    return a + b

# On définit une fonction qui calcule le carre d'un nombre
def carre(x):
    # On retourne le resultat de la multiplication du nombre par lui-meme
    return x * x

# Programme principal
if __name__ == "__main__":
    # On crée deux variables
    nombre1 = 5
    nombre2 = 3

    # On affiche la somme des deux nombres
    print("La somme est :", addition(nombre1, nombre2))

    # On affiche le carré du premier nombre
    print("Le carré de", nombre1, "est :", carre(nombre1))
