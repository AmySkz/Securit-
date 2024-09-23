
#partie 1
message = "esmhQVGXIPE"
cle = "cle"

def generer_cle(message,cle):
    cle_rep = cle*(len(message)//len(cle))+cle[:len(message)%len(cle)]
    return cle_rep

def chiff_vig(message,cle):
    res = ""
    cle = generer_cle(message,cle)
    for i in range(len(message)):
        asc = ord(message[i])
        if asc == 32:
            res+= " "
        elif message[i].islower():
            dec = ord(cle[i].lower()) - 97
            res += chr((asc -97 + dec)%26 + 97)
        elif message[i].isupper():
            dec = ord(cle[i].upper()) - 65
            res += chr((asc -65 + dec)%26 + 65)
        else:
            res += message[i]
    return res

def dechiff_vig(message,cle):
    res = ""
    cle = generer_cle(message,cle)
    for i in range(len(message)):
        asc = ord(message[i])
        if asc == 32:
            res+= " "
        elif message[i].islower():
            dec = ord(cle[i].lower()) - 97
            res += chr((asc -97 - dec)%26 + 97)
        elif message[i].isupper():
            dec = ord(cle[i].upper()) - 65
            res += chr((asc -65 - dec)%26 + 65)
        else:
            res += message[i]
    return res

print(dechiff_vig(message, cle))

#partie 2
#test Kasiski

