# Change Log

## Non publié

- `plot_curve_grid(..., vlines=...)` : chaque repère devient
  `(valeur, étiquette, couleur)` au lieu de `(valeur, étiquette)` —
  rupture d'API mineure (acceptable tant que la version majeure vaut 0),
  nécessaire pour distinguer visuellement plusieurs repères (ex. une
  fréquence de coupure optique et une fréquence d'échantillonnage, dans
  deux couleurs différentes).

## 0.1.0 (2026-10-24)

- Première version. Extrait d'`eoqual-phaseretrieval` : `plot_array`
  (heatmap 2D, ex-`io_utils.plot_array_plotly`) et `plot_curve_grid`
  (comparaison de courbes/coupes 1D avec repères verticaux,
  généralisation de l'ancien `io_utils.plot_mtf_cuts`, dont la partie
  spécifique à la FTM — extraction des coupes, fréquence de coupure —
  reste dans `eoqual-phaseretrieval`).
