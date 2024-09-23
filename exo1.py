#partie 1
text_a_chiffre = input("entrez un texte a chiffrer : ")
dec = int(input("entrer un nombre de decalage :"))

def chiff(message) :
    res = ""
    for lettre in message:
        asc = ord(lettre)
        if (asc == 32):
            res += " "
        elif (lettre.islower()):
            res += chr((asc - 97 + dec)% 26 + 97)
        elif (lettre.isupper()):
            res += chr((asc - 65 + dec)% 26 + 65)
        else :
            res+= lettre
        
    print(res)    

chiff(text_a_chiffre)

#partie 2

text_a_dechiffre = input("entrez un texte a dechiffrer : ")
dec_de = int(input("entrer un nombre de decalage :"))

def dechiff(message,dec_de) :
    res = ""
    for lettre in message:
        asc = ord(lettre)
        if (asc == 32):
            res += " "
        elif (lettre.islower()):
            res += chr((asc - 97 - dec_de)% 26 + 97)
        elif (lettre.isupper()):
            res += chr((asc - 65 - dec_de)% 26 + 65)
        else :
            res+= lettre
        
    return res    

print(dechiff(text_a_dechiffre,dec_de))

#partie 3
dechiffrements = []
print("Essai de toutes les clés possibles (1 à 25):\n")
for d in range(1, 26):
    text = dechiff(text_a_dechiffre, d)
    # stocker la cle et le déchiffrement
    dechiffrements.append((d, text)) 
#    print(f"Clé {d}: {text}")

#partie 4
#les mots sont en minuscule et separes par des espaces
def charger_fichier(f):
    with open(f,'r',encoding='utf-8') as file:
        contenu = file.read().strip()
        dictionnaire = set(contenu.split())
    return dictionnaire
#source du fichier : github
#https://github.com/Taknok/French-Wordlist/blob/master/francais.txt
dictionnaire = charger_fichier('francais.txt')

#variables pour stocker le meilleur dechiffrement
meilleur_score = 0
meilleur_dechiff = ""

#fonction pour compter des mots valides
def compte_mots_valides(texte, dictionnaire):
    # diviser le texte en mots et retirer la ponctuation directement dans la boucle
    mots = texte.lower().split()
    return sum(1 for mot in mots if mot.strip(".,!?:;") in dictionnaire)



print("\nAnalyse pour trouver le texte clair le plus probable:\n")
for dec, texte in dechiffrements:
    score = compte_mots_valides(texte, dictionnaire)
    print(f"Cle {dec}: {texte} (Mots valides: {score})")
    if score > meilleur_score:
        meilleur_score = score
        meilleur_dechiff = texte

# affichage du meilleur dechiffrement
print(f"\nLe texte clair le plus probable est :\n{meilleur_dechiff}")

