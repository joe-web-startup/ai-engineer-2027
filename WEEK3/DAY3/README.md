# Week 3 · Day 3 — La classification : prédire OUI ou NON

## Ce que j'ai appris
- Régression = prédire un nombre ; classification = prédire une catégorie (0 / 1).
- La régression logistique : un score linéaire passé dans la sigmoïde, qui donne une probabilité.
- `predict` (0 ou 1) et `predict_proba` (la probabilité).
- La matrice de confusion, l'accuracy, la precision et le recall, et quand privilégier l'une ou l'autre.
- Toujours battre la baseline ; avec des classes déséquilibrées, l'accuracy seule ment.

## Ce que j'ai fait (dans ExamPredict AI)
| Fichier | Résultat |
|---|---|
| `exampredict-ai/src/classer_2027.py` | Classifieur « ce chapitre tombe-t-il ? » en physique-chimie : accuracy 0,70 contre 0,50 pour la baseline, sur 2024–2026 ; mécanique et chimie organique à 76 % pour 2027 |

## Fiche de cours
- [F1.DAY3.WEEK3 · La classification](cours/F1.DAY3.WEEK3.pdf)
