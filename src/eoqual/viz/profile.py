#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comparaison de profils/coupes 1D (Plotly) — un ou plusieurs sous-graphes
côte à côte, partageant le même axe des abscisses, chacun comparant une
courbe "estimée" à une courbe "référence" optionnelle, avec d'éventuels
repères verticaux (ex. une fréquence de coupure).
"""

from __future__ import annotations

from typing import List, Optional, Sequence, Tuple

import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_curve_grid(
    x: np.ndarray,
    panels: Sequence[Tuple[str, np.ndarray]],
    *,
    references: Optional[Sequence[Optional[np.ndarray]]] = None,
    vlines: Optional[Sequence[Tuple[float, str, str]]] = None,
    xlabel: str = "",
    ylabel: str = "",
    title: str = "",
    estimated_label: str = "Estimée",
    reference_label: str = "Référence",
    estimated_color: str = "crimson",
    reference_color: str = "black",
    x_range: Optional[Tuple[float, float]] = None,
    y_range: Optional[Tuple[float, float]] = None,
    width: Optional[int] = None,
    height: int = 380,
) -> go.Figure:
    """
    Compare une ou plusieurs courbes "estimées" à leur "référence"
    optionnelle, sur un axe des abscisses partagé — typiquement des
    coupes (horizontale/verticale) d'un champ 2D (PSF, FTM, carte de
    WFE...), mais la fonction ne suppose rien de spécifique : ``x``/les
    courbes de ``panels`` sont de simples tableaux 1D.

    Parameters
    ----------
    x : NDArray
        Axe des abscisses, partagé par tous les sous-graphes.
    panels : sequence of (str, NDArray)
        Un ``(titre_du_sous_graphe, courbe_estimée)`` par sous-graphe,
        dans l'ordre d'affichage (de gauche à droite).
    references : sequence of NDArray or None, optional
        Une courbe de référence par sous-graphe (même ordre que
        ``panels``), ou ``None`` à une position donnée pour ne pas
        tracer de référence sur ce sous-graphe précis. ``None`` (défaut)
        global : aucune référence nulle part (pas de vérité terrain
        disponible).
    vlines : sequence of (float, str, str), optional
        Repères verticaux ``(valeur, étiquette, couleur)`` tracés sur
        **tous** les sous-graphes — ex. une fréquence de coupure dans une
        couleur, une fréquence d'échantillonnage dans une autre. ``None``
        (défaut) : aucun repère.
    xlabel, ylabel : str, optional
        Légendes des axes (partagées par tous les sous-graphes).
    title : str, optional
        Titre de la figure.
    estimated_label, reference_label : str, optional
        Légende des courbes dans la légende de la figure.
    estimated_color, reference_color : str, optional
        Couleur des courbes (nom Plotly/CSS, ou code hexadécimal).
    x_range : tuple of (float, float), optional
        Limites de l'axe des abscisses, partagées par tous les
        sous-graphes — utile pour garantir qu'un repère de ``vlines``
        situé hors de la plage couverte par ``x`` reste visible. ``None``
        (défaut) : échelle automatique (uniquement sur l'étendue de
        ``x`` — un repère hors de cette étendue ne serait alors pas
        visible).
    y_range : tuple of (float, float), optional
        Limites de l'axe des ordonnées, partagées par tous les
        sous-graphes. ``None`` (défaut) : échelle automatique.
    width : int, optional
        Largeur de la figure [px]. ``None`` (défaut) : ``350 * n_panels``.
    height : int, default 380
        Hauteur de la figure [px].

    Returns
    -------
    go.Figure
        Figure Plotly à ``n_panels`` sous-graphes côte à côte, prête pour
        ``.show()``.

    Raises
    ------
    ValueError
        Si ``references`` est fourni avec une longueur différente de
        ``panels``.
    """
    n = len(panels)
    if references is not None and len(references) != n:
        raise ValueError(
            f"references a {len(references)} élément(s), attendu {n} (autant que panels)."
        )

    fig = make_subplots(rows=1, cols=n, subplot_titles=[title for title, _ in panels])

    for col, (_, y_est) in enumerate(panels, start=1):
        fig.add_scatter(
            x=x, y=y_est, name=estimated_label, line=dict(color=estimated_color),
            showlegend=(col == 1), row=1, col=col,
        )
        y_ref = references[col - 1] if references is not None else None
        if y_ref is not None:
            fig.add_scatter(
                x=x, y=y_ref, name=reference_label,
                line=dict(color=reference_color, dash="dash"),
                showlegend=(col == 1), row=1, col=col,
            )

    if vlines:
        for col in range(1, n + 1):
            for value, label, color in vlines:
                fig.add_vline(
                    x=value, line=dict(color=color, dash="dot"),
                    annotation_text=label, annotation_position="top", row=1, col=col,
                )

    fig.update_xaxes(title_text=xlabel, range=x_range)
    fig.update_yaxes(title_text=ylabel, range=y_range)
    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor="center"),
        width=width or 350 * n,
        height=height,
        margin=dict(l=0, r=0, t=60, b=0),
    )
    return fig
