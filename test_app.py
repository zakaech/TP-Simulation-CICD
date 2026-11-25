import pytest
from app import calculer_moyenne, mention, est_admis


def test_calculer_moyenne():
    assert calculer_moyenne([12, 14, 16]) == 14


def test_liste_notes_vide():
    with pytest.raises(ValueError):
        calculer_moyenne([])


def test_mention():
    assert mention(17) == "Très bien"
    assert mention(15) == "Bien"
    assert mention(13) == "Assez bien"
    assert mention(11) == "Passable"
    assert mention(8) == "Ajourné"


def test_est_admis():
    assert est_admis(12) is True
    assert est_admis(8) is False