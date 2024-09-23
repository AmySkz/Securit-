import zipfile
import itertools
import string

# Fonction pour tenter d'extraire le fichier de l'archive avec un mot de passe donné
def tenter_mot_de_passe(archive, mot_de_passe):
    try:
        # Tentative d'extraction avec le mot de passe
        archive.extractall(pwd=mot_de_passe.encode('utf-8'))
        print(f"Mot de passe trouvé : {mot_de_passe}")
        return True
    except:
        return False

# Fonction principale pour tester tous les mots de passe possibles
def brute_force_zip(archive_path):
    # Charger l'archive zip
    archive = zipfile.ZipFile(archive_path)

    # Lettres minuscules à utiliser pour générer les combinaisons
    lettres = string.ascii_lowercase

    # Test des mots de passe de longueur 1 à 6 (par exemple)
    for longueur in range(1, 3):
        # Générer toutes les combinaisons possibles de la longueur actuelle
        for combinaison in itertools.product(lettres, repeat=longueur):
            mot_de_passe = ''.join(combinaison)
            
            
            # Essayer d'ouvrir l'archive avec ce mot de passe
            if tenter_mot_de_passe(archive, mot_de_passe):
                return

# Chemin vers l'archive ZIP protégée par mot de passe
archive_path = 'IntroSecu_TP1.zip'

# Lancer l'attaque brute force
brute_force_zip(archive_path)
