import string
import math
import pwinput
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


def donner_conseils(analyse):
        conseils = []
        if not analyse["minuscules"]:
                conseils.append("Ajoutez des lettres minuscules")
        if not analyse["majuscules"]:
                conseils.append("Ajoutez des lettres majuscules")
        if not analyse["chiffres"]:
                conseils.append("Ajoutez des chiffres")
        if not analyse["symboles"]:
                conseils.append("Ajoutez des symboles")
        if analyse["longueur"] < 6:
                conseils.append("Veuillez saisir un mot de passe plus long")
        return conseils
        
def evaluer_robustesse(bits):
        if bits > 60:
                return "Fort"  
        elif bits > 40 and bits <= 60:
                return "Moyen"     
        else:
                return "Faible"


        

                
if __name__ == "__main__":               
        mot_de_passe = pwinput.pwinput("Saissisez votre mot de passe : ")
        analyse = analyser_composition(mot_de_passe)
        bits = calculer_entropie(analyse)
        conseils = donner_conseils(analyse)
        niveau = evaluer_robustesse(bits)

        print(f"Longueur : {analyse['longueur']}")
        print(f"Minuscules : {'oui' if analyse['minuscules'] else 'non'}")
        print(f"Majuscules : {'oui' if analyse['majuscules'] else 'non'}")
        print(f"Chiffres : {'oui' if analyse['chiffres'] else 'non'}")
        print(f"Symboles : {'oui' if analyse['symboles'] else 'non'}")
        print(f"Entropie : {bits:.1f} bits")
        print(f"Niveau : {niveau}")
        if conseils:
                print("Conseils pour l'améliorer :")
                for conseil in conseils:
                        print(f"- {conseil}")

        
        




        

        











