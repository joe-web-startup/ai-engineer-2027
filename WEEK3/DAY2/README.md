# Week 3 · Day 2 — Premier modèle de Machine Learning avec scikit-learn

## Ce que j'ai appris
- Un modèle de ML apprend sa règle à partir d'exemples : `model.fit(X, y)`.
- **X** = les entrées (features), **y** = la cible. Préparer les features, c'est le **feature engineering**.
- La **régression linéaire** prédit une somme pondérée ; `model.coef_` donne les poids appris.
- Données dans le temps → couper **train / test dans le temps**, jamais au hasard.
- La **MAE** mesure l'erreur moyenne ; un modèle doit battre le pif.
- Trop peu de données → les stats battent le ML ; le remède, c'est plus de données.

## Ce que j'ai fait (dans ExamPredict AI)
| Fichier | Résultat |
|---|---|
| `exampredict-ai/src/modele_2027.py` | Régression linéaire pour physique-chimie, maths et SVT : bat le pif dans les 3 matières (maths 0,76 contre 1,22) |
| `exampredict-ai/src/predire_par_jour.py` | Prédiction 2027 jour 1 / jour 2 avec moyenne, médiane, écart-type depuis la réforme |
| `exampredict-ai/data/chapitres_bac.csv` | Ajout des maths et des SVT, suppression de 2021 (épreuves annulées, vérifié) |

## Fiche de cours
- [F1.DAY2.WEEK3 · Premier modèle de ML avec scikit-learn](cours/F1.DAY2.WEEK3.pdf)
