# Week 3 · Day 4 — Lire n'importe quel dossier de sujets PDF

## Ce que j'ai appris
- Extraire le texte d'un PDF avec `pypdf`, puis le découper en exercices avec une expression régulière.
- Le ML non supervisé (TF-IDF) repère le décor d'un exercice (« roche », « bille »), pas la notion du programme.
- Un seuil (au moins 3 mots-clés) supprime les fausses détections de thèmes, comme le seuil de décision du Day 3.
- Écrire des modules remplaçables : la détection des thèmes pourra être confiée à Claude sans toucher au reste.
- Protéger un secret : `.env`, `.gitignore`, `.env.example`, et `git add` fichier par fichier.

## Ce que j'ai fait (dans ExamPredict AI)
| Fichier | Rôle |
|---|---|
| `exampredict-ai/src/pdf_sujets.py` | Analyse un dossier de PDF : exercices, points, thèmes, thèmes les plus fréquents |
| `exampredict-ai/src/lire_sujet_ia.py` | Version Claude (sortie JSON structurée), prête pour quand la clé API sera branchée |
| `exampredict-ai/src/verifier_cles.py` | Vérifie quelles clés API ont du crédit, sans jamais les afficher |
