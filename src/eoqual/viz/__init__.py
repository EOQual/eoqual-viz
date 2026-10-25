"""
eoqual.viz — fonctions graphiques génériques (Plotly) partagées par les
modules EOQual.

Public API
----------
>>> from eoqual.viz import plot_array, plot_curve_grid
>>> plot_array(image, log=True).show()
>>> plot_curve_grid(
...     freq, [("Coupe H", cut_h), ("Coupe V", cut_v)],
...     references=[cut_h_ref, cut_v_ref], vlines=[(1.0, "fc")],
... ).show()

Voir ``README.md`` pour le catalogue et les règles de ce paquet.
"""

__version__ = "0.1.0"
__title__ = "eoqual.viz"
__description__ = "Generic Plotly visualisation helpers shared across EOQual modules"
__url__ = "https://github.com/EOQual/eoqual-viz"
__uri__ = __url__
__doc__ = __description__ + " <" + __uri__ + ">"
__author__ = "Olivier Amram"
__email__ = "olivier.amram@free.fr"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2026 Olivier Amram"

from .heatmap import plot_array  # noqa: F401
from .profile import plot_curve_grid  # noqa: F401

__all__ = [
    "plot_array",
    "plot_curve_grid",
]
