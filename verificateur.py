import string
import math
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
                
                



print(calculer_entropie(analyser_composition("()#")))      
print(calculer_entropie(analyser_composition("abcdefgh")))
print(calculer_entropie(analyser_composition("")))
#print(analyser_composition("ABC123"))
#print(analyser_composition("Exemple#2026"))




