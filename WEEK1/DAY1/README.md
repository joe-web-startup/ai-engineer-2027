# Week 1 · Day 1 — Comprendre ce que Python fait vraiment

## Ce que j'ai appris
- Une variable est une **étiquette** sur un objet : `b = a` ne copie rien.
- **Mutable / immuable** : une liste se modifie sur place, un nombre ou un texte jamais.
- **Copie superficielle / profonde** : `.copy()` et `deepcopy()`.
- **Effet de bord** : une fonction qui modifie ses entrées en cachette peut fausser les données d'une IA.
- `enumerate`, `zip`, les compréhensions, `sorted`, `Counter`, `defaultdict`.
- La **complexité Big O** : O(1), O(n), O(n log n), O(n²).
- L'architecture d'une IA de prédiction d'examens : pipeline, backtesting, précision@k, grid search.

## Ce que j'ai fait
- `exercices/ex1_1.py` : prouver avec `id()` et `is` que deux noms pointent vers le même objet.
- `exercices/ex1_5.py` : corriger un bug d'effet de bord dans `normaliser_notes` (`notes.copy()`).
- Sur **ExamPredict AI** : écrire `count_keyword`, qui corrige la détection du « ph » trouvé à tort dans « physique ».

## Fiches de cours
- [F1.DAY1.WEEK1 · Modèle mémoire Python](cours/F1.DAY1.WEEK1.pdf)
- [F2.DAY1.WEEK1 · Compter, filtrer, trier et mesurer](cours/F2.DAY1.WEEK1.pdf)
- [F3.DAY1.WEEK1 · ExamPredict AI : construire le cerveau](cours/F3.DAY1.WEEK1.pdf)
