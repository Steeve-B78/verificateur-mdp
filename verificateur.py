import string
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
    return a_minuscule, a_majuscule, a_chiffre, a_symbole

        

print(analyser_composition("abc"))
print(analyser_composition("ABC123"))
print(analyser_composition("Exemple#2026"))
print(analyser_composition(""))



