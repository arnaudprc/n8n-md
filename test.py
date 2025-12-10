# Exemple de programme Python avec commentaires basiques

# On définit une fonction qui calcule la somme de deux nombres
def addition(a, b):
    # On retourne le résultat de l'addition
    return a + b

# On définit une fonction qui calcule le carré d'un nombre
def carre(x):
    # On retourne le résultat de la multiplication du nombre par lui-même
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
