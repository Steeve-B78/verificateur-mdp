import string
#print(string.ascii_lowercase)
#print(string.digits)


def analyser_composition(mdp):
    a_minuscule = False
    for c in mdp:
        if c in string.digits:
            a_minuscule = True
    return a_minuscule

        

print(analyser_composition("abc"))
print(analyser_composition("123"))
print(analyser_composition("ABC"))
print(analyser_composition("123abc"))



