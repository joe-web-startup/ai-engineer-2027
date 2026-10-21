# MINI-PROJET · L'analyseur de notes (fiche F2.DAY3.WEEK1, sections 9 et 10)
#
# Construis UNE fonction à la fois, dans l'ordre. Après chacune :
# Ctrl + S, puis  py analyseur.py  → les tests de cette fonction doivent passer.
# Lance depuis le dossier projet :  cd projet   puis   py analyseur.py

import json


def lire_lignes(chemin):
    """Renvoie la liste des lignes non vides du fichier, sans espaces au bord.
    Si le fichier n'existe pas : affiche un message clair et renvoie []."""
    pass  # ✍️


def analyser_ligne(ligne):
    """'Lina;14' → ('Lina', 14.0)
    Lève ValueError("format attendu nom;note")   s'il n'y a pas exactement 2 morceaux,
    Lève ValueError("note non numérique")        si la note n'est pas un nombre,
    Lève ValueError(f"note hors limites : {note}") si la note n'est pas entre 0 et 20."""
    pass  # ✍️


def charger_notes(chemin):
    """Renvoie (valides, rejets) :
    valides = liste de (nom, note)
    rejets  = liste de (ligne, raison)"""
    pass  # ✍️


def statistiques(valides):
    """Renvoie un dictionnaire avec les clés :
    'effectif', 'moyenne' (arrondie à 2 décimales), 'max' (nom, note),
    'min' (nom, note), 'admis' (nombre de notes >= 10)"""
    pass  # ✍️


def sauver_json(donnees, chemin):
    """Écrit donnees dans le fichier chemin au format JSON (indent=2, accents gardés)."""
    pass  # ✍️


def afficher_rapport(stats, rejets):
    """Le SEUL endroit du programme qui contient des print."""
    pass  # ✍️


# ----- Tests : décommente chaque groupe quand sa fonction est écrite -----
if __name__ == "__main__":
    # lire_lignes
    # assert lire_lignes("absent.txt") == []
    # assert len(lire_lignes("notes_classe.txt")) == 10

    # analyser_ligne
    # assert analyser_ligne("Lina;14") == ("Lina", 14.0)
    # for mauvaise in ["Yanis;abc", "Tom;22", "sans point virgule"]:
    #     try:
    #         analyser_ligne(mauvaise)
    #         assert False, f"{mauvaise} aurait dû être refusée"
    #     except ValueError:
    #         pass

    # charger_notes
    # valides, rejets = charger_notes("notes_classe.txt")
    # assert len(valides) == 6 and len(rejets) == 4

    # statistiques
    # s = statistiques(valides)
    # assert s["effectif"] == 6 and s["moyenne"] == 12.67 and s["admis"] == 4
    # assert s["max"] == ("Chloé", 17.0) and s["min"] == ("Jules", 8.0)

    # Programme complet
    # afficher_rapport(s, rejets)
    # sauver_json({"statistiques": s, "rejets": rejets}, "rapport.json")
    # print("✅ Mini-projet validé")
    pass
