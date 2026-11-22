from verificateur import analyser_composition, calculer_entropie, evaluer_robustesse, donner_conseils
import pytest


def test_analyse_majuscules_et_chiffres():
    a = analyser_composition("ABC123")
    assert a == {"longueur": 6,  
                          "minuscules": False, 
                          "majuscules": True, 
                          "chiffres": True, 
                          "symboles": False}


def test_analyse_chaîne_vide():
    b = analyser_composition("")
    assert b == {"longueur": 0,  
                          "minuscules": False, 
                          "majuscules": False, 
                          "chiffres": False, 
                          "symboles": False}

def test_analyse_symboles():
    c = analyser_composition("()#*")
    assert c == {"longueur": 4,  
                              "minuscules": False, 
                              "majuscules": False, 
                              "chiffres": False, 
                              "symboles": True}

def test_entropie_symboles():
    analyse = analyser_composition("()#")
    assert calculer_entropie(analyse)== pytest.approx(15)

def test_entropie_minuscules():
    analyse = analyser_composition("abcdefgh")
    assert calculer_entropie(analyse)== pytest.approx(37.603517745128734)

def test_entropie_chaîne_vide():
    analyse = analyser_composition("")
    assert calculer_entropie(analyse)== pytest.approx(0)

def test_entropie_all():
    analyse = analyser_composition("Aa1#")
    assert calculer_entropie(analyse)== pytest.approx(26.21835540671055)


def test_robustesse_faible():
    seuils = 40
    assert evaluer_robustesse(seuils) == "Faible"


def test_robustesse_fort():
    seuils = 80
    assert evaluer_robustesse(seuils) == "Fort"

def test_robustesse_moyen():
    seuils = 50
    assert evaluer_robustesse(seuils) == "Moyen"

def test_robustesse_limite_60_bits():
    seuils = 60
    assert evaluer_robustesse(seuils) == "Moyen"


def test_conseils_mot_de_passe_complet():
    analyse = analyser_composition("1234@#Stv78")
    assert donner_conseils(analyse) == []

def test_conseils_chaîne_vide():
    analyse = analyser_composition("")
    assert len(donner_conseils(analyse)) == 5

def test_conseils_sans_symboles():
    analyse = analyser_composition("1234Attention")
    assert "Ajoute des symboles" in donner_conseils(analyse)


def test_conseils_mot_de_passe_court():
    analyse = analyser_composition("1Ab#O")
    assert "Veuillez saisir un mot de passe plus long" in donner_conseils(analyse)

def test_conseil_longueur_limite_6():
    analyse = analyser_composition("2Bc#IH")
    assert "Veuillez saisir un mot de passe plus long" not in donner_conseils(analyse)


