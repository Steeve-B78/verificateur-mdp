from verificateur import analyser_composition, calculer_entropie
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



