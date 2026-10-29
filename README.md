<p align="center">
  <img src="https://raw.githubusercontent.com/EOQual/pixoscope/main/resources/eoqual_rounded.png" alt="EOQual" width="280">
</p>

# eoqual-viz

Fonctions graphiques **génériques** (Plotly) communes aux modules EOQual :
heatmap 2D interactive, comparaison de profils/coupes 1D avec repères
verticaux. Extrait d'`eoqual-phaseretrieval` (où ces fonctions n'avaient
rien de spécifique à la récupération de phase) pour être réutilisable
sans dépendre de ce paquet.

**Ce n'est pas** un visualisateur d'images autonome — pour ça, voir
[pixoscope](https://github.com/EOQual/pixoscope) (application à part
entière, pas une bibliothèque). `eoqual-viz` ne fournit que des
fonctions Python qui construisent une figure Plotly, à appeler depuis
votre propre code/notebook.

## Sommaire

1. [Installation](#installation)
2. [Contenu](#contenu)
3. [Règles](#règles)
4. [Utilisateurs](#utilisateurs)
5. [Licence](#licence)

---

## Installation

```bash
pip install git+https://github.com/EOQual/eoqual-viz.git
```

Dépendances : numpy et plotly, rien d'autre.

## Contenu

| Module | Fonctions | Usage typique |
|---|---|---|
| `eoqual.viz.heatmap` | `plot_array` | Afficher un tableau 2D (PSF, masque, carte de phase...) en heatmap interactive, échelle log optionnelle |
| `eoqual.viz.gallery` | `plot_image_grid` | Comparer plusieurs images côte à côte (observée, restaurée, référence), à échelle commune |
| `eoqual.viz.curves` | `plot_curves` | Plusieurs courbes `y(x)` sur un graphe, axes log optionnels (convergence, critère en fonction d'un paramètre) |
| `eoqual.viz.profile` | `plot_curve_grid` | Comparer une ou plusieurs courbes "estimées" à une référence optionnelle, sur un axe partagé, avec repères verticaux (ex. une fréquence de coupure) |

```python
from eoqual.viz import plot_array, plot_curve_grid

plot_array(psf, log=True, title="PSF (log)").show()

plot_curve_grid(
    freq, [("Coupe horizontale", cut_h), ("Coupe verticale", cut_v)],
    references=[cut_h_ref, cut_v_ref],
    vlines=[(1.0, "fc")],
    xlabel="Fréquence réduite (fraction de fe/2)", ylabel="FTM",
).show()
```

## Règles

Ce paquet est une dépendance des autres modules : il doit rester léger et
générique.

- **numpy et plotly seulement** — pas de dépendance à un module métier
  (pas d'optique, de Zernike, de Bayer...) ;
- **fonctions pures** sur tableaux + paramètres d'affichage : pas
  d'entrées/sorties fichier, de CLI, ni de journalisation ; une fonction
  renvoie toujours une `go.Figure`, jamais ne l'affiche elle-même
  (`.show()` reste à l'appelant) ;
- une fonction n'entre ici que si elle ne suppose **rien de spécifique**
  à un domaine métier (une courbe, un axe, une étiquette — jamais une
  PSF, une FTM ou une pupille par leur nom) ;
- **API stable** : les modules consommateurs fixent une plage de version,
  comme pour `eoqual-core`.

Les fonctions qui assemblent des données **spécifiques à un domaine**
(ex. extraire les coupes H/V d'une FTM, calculer sa fréquence de
coupure) n'ont pas leur place ici : elles restent dans le module métier
concerné (ex. `eoqual.phaseretrieval.diagnostics`), qui appelle ensuite
`eoqual.viz` avec les tableaux déjà préparés.

## Utilisateurs

| Module | Fonctions utilisées |
|---|---|
| eoqual-phaseretrieval | `plot_array` (PSF, masque, cartes de phase), `plot_curve_grid` (coupes PSF/FTM) |
| eoqual-deconvolution | `plot_image_grid` (résultats), `plot_curves` (convergence, réglage), `plot_array` (PSF) |

## Licence

MIT — voir `license.txt` et `THIRD_PARTY_LICENSES.md`.
