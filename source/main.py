# This is a sample Python script.
import random


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def convertir(valeur=0):
    if valeur == 19 :
        return "deez nuts"
    elif valeur < 100:
        return nombre(valeur)
    elif valeur < 1000:
        return truc_aine(valeur, 100, 1000, "cent")
    elif valeur < 1000000:
        return truc_aine(valeur, 1000, 1000000, "mille")
    elif valeur < 1000000000:
        return truc_llion(valeur, 1000000, 1000000000, "million")
    elif valeur < 1000000000000:
        return truc_llion(valeur, 1000000000, 1000000000000, "milliard")
    return "non"


def truc_llion(valeur=0, cent=100, max=1000, nom="cent"):
    if valeur < max:
        if int(valeur / cent) > 1:
            nom += "s"
        if valeur - (int(valeur / cent) * cent) == 0:
            return convertir(int(valeur / cent)) + "-" + nom
        return convertir(int(valeur / cent)) + "-" + nom + "-" + convertir(valeur - (int(valeur / cent) * cent))


def truc_aine(valeur=0, cent=100, max=1000, nom="cent"):
    if valeur == cent:
        return nom
    elif valeur < (2 * cent):
        return nom + "-" + convertir(valeur - (int(valeur / cent) * cent))
    elif valeur < max:
        if valeur - (int(valeur / cent) * cent) == 0:
            return convertir(int(valeur / cent)) + "-" + nom
        return convertir(int(valeur / cent)) + "-" + nom + "-" + convertir(valeur - (int(valeur / cent) * cent))


def nombre(valeur=0):
    if valeur < 10:
        return chiffre(valeur)
    elif valeur == 10:
        return "dix"
    elif valeur == 11:
        return "onze"
    elif valeur == 12:
        return "douze"
    elif valeur == 13:
        return "treize"
    elif valeur == 14:
        return "quatorze"
    elif valeur == 15:
        return "quinze"
    elif valeur == 16:
        return "seize"
    elif valeur == 20:
        return "vingt"
    elif valeur == 30:
        return "trente"
    elif valeur == 40:
        return "quarante"
    elif valeur == 50:
        return "cinquante"
    elif valeur == 60:
        return "soixante"
    else:
        valeurTest = 10
        while valeurTest < 100:
            if valeurTest < 70:
                if valeur < valeurTest + 10:
                    if valeur - valeurTest == 1:
                        return nombre(valeurTest) + "-et-un"
                    return nombre(valeurTest) + "-" + nombre(valeur - valeurTest)
            elif valeur < 80:
                if valeur - 70 == 1:
                    return nombre(60) + "-et-onze"
                return nombre(60) + "-" + nombre(valeur - 60)
            else:
                if valeur - 80 == 0:
                    return nombre(4) + "-" + nombre(20)
                return nombre(4) + "-" + nombre(20) + "-" + nombre(valeur - 80)
            valeurTest += 10
        return "zero"


def chiffre(chiffre=0):
    if (chiffre == 0):
        return "zero"
    elif (chiffre == 1):
        return "un"
    elif (chiffre == 2):
        return "deux"
    elif (chiffre == 3):
        return "trois"
    elif (chiffre == 4):
        return "quatre"
    elif (chiffre == 5):
        return "cinq"
    elif (chiffre == 6):
        return "six"
    elif (chiffre == 7):
        return "sept"
    elif (chiffre == 8):
        return "huit"
    elif (chiffre == 9):
        return "neuf"
    else:
        return ""


if __name__ == "__main__":
    monNombre = random.randint(0,999999999999)
    print(monNombre)
    print(convertir(monNombre))
