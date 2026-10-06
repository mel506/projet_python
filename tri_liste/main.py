choix = input("Voulez vous ranger par ordre croissant ou decroissant? ")
choix1 = "croissant"
choix2 = "decroissant"
def  tri_liste(liste) :
    if choix == choix1 :
    # Tri ordre croissant
        for i in range(1,len(liste)):
            valeur = liste[i]
            j = i - 1
    # Compare les valeurs de la liste
            while j >= 0 and liste[j] > valeur :
    # Permutation de valeurs
                liste[j + 1] = liste[j]
                j = j - 1
            liste[j + 1] = valeur
        return liste
    else  :
    # Tri ordre decroissant
        for i in range(1,len(liste)) :
            valeur = liste[i]
            j = i - 1
            while j >= 0 and liste[j] < valeur :
                liste[j + 1] = liste[j]
                j = j - 1
            liste[j + 1] = valeur
        return liste
A = [7,0,9,1,10,3]
if choix == choix1:
    result = tri_liste(A)
    print("Ordre croissant:",result)
else:
    result = tri_liste(A)
    print("Ordre decroissant:",result)
print()
# Ranger par ordre alphabétique
def tri_alpha(nom):
    for i in range(1,len(nom)):
        for j in range(i,len(nom)):
            mot1 = nom[i-1]
            mot2 = nom[j]
            
            if mot1 > mot2:
                X = nom[i-1]
                nom[i-1] = nom[j]
                nom[j] = X
    return nom
N = ["Thomas","Ange","Manuelle","Emma","Alice"]
result = tri_alpha(N)
print("Ordre alphabétique:",result)
