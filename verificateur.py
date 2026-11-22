import string
import math
import pwinput
import pytest
#print(string.ascii_lowercase)  # "abc"
#print(string.digits)           # "123"
#print(string.ascii_uppercase)  # "ABC"
#print(string.punctuation)      # "%&*()"




def analyser_composition(mdp):
    a_minuscule = False
    a_majuscule = False
    a_chiffre = False
    a_symbole = False
    

    for c in mdp:
        if c in string.ascii_lowercase:
            a_minuscule = True
        if c in string.ascii_uppercase:
                    a_majuscule = True
        if c in string.digits:
                    a_chiffre = True
        if c in string.punctuation:
                    a_symbole = True

    d ={"longueur": len(mdp),  
                          "minuscules": a_minuscule, 
                          "majuscules": a_majuscule, 
                          "chiffres": a_chiffre, 
                          "symboles": a_symbole}
    return d

def calculer_entropie(analyse):
        taille = 0
        if analyse["minuscules"] == True:
                taille +=26
        if analyse["majuscules"] == True:
                        taille +=26
        if analyse["chiffres"] == True:
                        taille +=10
        if analyse["symboles"] == True:
                        taille += 32     
        if taille == 0:
                return 0 
        return analyse["longueur"]*math.log2(taille)
                
if __name__ == "__main__":               
        mot_de_passe = pwinput.pwinput("Saissisez votre mot de passe : ")
        analyse = analyser_composition(mot_de_passe)
        bits = calculer_entropie(analyse)

        print(f"Longueur : {analyse['longueur']}")
        print(f"Minuscules : {'oui' if analyse['minuscules'] else 'non'}")
        print(f"Majuscules : {'oui' if analyse['majuscules'] else 'non'}")
        print(f"Chiffres : {'oui' if analyse['chiffres'] else 'non'}")
        print(f"Symboles : {'oui' if analyse['symboles'] else 'non'}")
        print(f"Etropie : {bits:.1f} bits")
        
        
        
        











