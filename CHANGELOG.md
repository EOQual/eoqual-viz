# Change Log

## Non publié

- Documentation Sphinx/autoapi (`docs/`), publiée sur GitHub Pages à
  chaque push sur `main` (`.github/workflows/docs.yml`), comme les autres
  modules EOQual.
- Tests lancés automatiquement par GitHub Actions
  (`.github/workflows/tests.yml`).

## 0.2.0 (2026-10-29)

- `plot_image_grid` (`gallery`) : galerie d'images 2D, ligne 0 en haut,
  pixels carrés, échelle de couleur commune ou propre à chaque image.
- `plot_curves` (`curves`) : plusieurs courbes `(étiquette, x, y)` sur un
  même graphe, axes linéaires ou logarithmiques, repères verticaux.

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
