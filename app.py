def calculer_moyenne(notes):
    if not notes:
        raise ValueError("La liste des notes est vide")
    return sum(notes) / len(notes)


def mention(moyenne):
    if moyenne >= 16:
        return "Très bien"
    elif moyenne >= 14:
        return "Bien"
    elif moyenne >= 12:
        return "Assez bien"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Ajourné"


def est_admis(moyenne):
    return moyenne >= 10