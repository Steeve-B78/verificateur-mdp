import string
#print(string.ascii_lowercase)  # "abc"
#print(string.digits)           # "123"
#print(string.ascii_uppercase)  # "ABC"
#print(string.punctuation)      # "%&*()"


def analyser_composition(mdp):
    a_minuscule = False
    for c in mdp:
        if c in string.ascii_lowercase:
            a_minuscule = True
    return a_minuscule

        

print(analyser_composition("abc"))
print(analyser_composition("123"))
print(analyser_composition("ABC"))
print(analyser_composition("123abc"))



