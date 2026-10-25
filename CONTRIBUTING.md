# Contribuer à eoqual-viz

Ce paquet est une dépendance des autres modules EOQual : chaque ajout se
paie en stabilité. Avant de proposer une fonction, vérifier les règles
du README :

- numpy et plotly seulement ;
- fonctions pures (tableaux + paramètres d'affichage), sans
  entrées/sorties ni journalisation ; renvoie une `go.Figure`, ne
  l'affiche jamais elle-même ;
- rien de spécifique à un domaine métier (pas de PSF, de FTM, de
  Zernike... par leur nom) — ces assemblages restent dans le module
  consommateur.

## Ajouter une fonction

1. Un module par famille de représentation (`heatmap`, `profile`...),
   `__all__` explicite, docstrings NumPy.
2. Des tests sur des figures Plotly simples (nombre de traces, données
   des axes, présence des repères) plutôt que des images de référence.
3. Une entrée dans `CHANGELOG.md` et une ligne dans le tableau du
   README. Toute modification de signature ou de comportement d'une
   fonction existante est une rupture d'API : version mineure suivante,
   et mention explicite.

## Licence

MIT — voir `license.txt`.

## Tests

```bash
PYTHONPATH=src pytest tests
```
