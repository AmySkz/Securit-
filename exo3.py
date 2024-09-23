import hashlib

def calculer_md5(chaine):
    """Calculer le haché MD5 d'une chaîne de caractères."""
    return hashlib.md5(chaine.encode()).hexdigest()

def trouver_mot_de_passe(hache, fichier_dictionnaire):
    """Trouver le mot de passe associé au haché MD5 en utilisant un fichier dictionnaire."""
    with open(fichier_dictionnaire, 'r', encoding='ISO-8859-1') as file:
        for ligne in file:
            mot_de_passe = ligne.strip()
            if calculer_md5(mot_de_passe) == hache:
                return mot_de_passe
    return None

# Haché MD5 à retrouver
hache_md5 = '5a74dd4eef347734c8a0a9a3188abd11'

# Fichier contenant les mots de passe courants
fichier_dictionnaire = 'rockyou.txt'  # Chemin vers le fichier rockyou.txt

# Trouver le mot de passe
mot_de_passe_trouve = trouver_mot_de_passe(hache_md5, fichier_dictionnaire)

if mot_de_passe_trouve:
    print(f"Le mot de passe associé au haché est : {mot_de_passe_trouve}")
else:
    print("Mot de passe non trouvé dans le dictionnaire.")
