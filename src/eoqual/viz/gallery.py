#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Galerie d'images 2D côte à côte (Plotly), à échelle de couleur commune
ou propre à chaque image.
"""

from __future__ import annotations

from typing import Optional, Sequence, Tuple

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_image_grid(
    images: Sequence[Tuple[str, np.ndarray]],
    *,
    ncols: Optional[int] = None,
    cmap: str = "gray",
    shared_scale: bool = True,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
    title: str = "",
    panel_size: int = 300,
) -> go.Figure:
    """
    Affiche plusieurs tableaux 2D en grille, une heatmap par tableau,
    ligne 0 en haut (convention image) et pixels carrés.

    Parameters
    ----------
    images : sequence of (str, NDArray)
        ``(titre, tableau_2D)`` dans l'ordre d'affichage (ligne par ligne).
    ncols : int, optional
        Nombre de colonnes. Défaut : toutes les images sur une ligne,
        jusqu'à 4 colonnes.
    cmap : str, default "gray"
        Nom du colormap Plotly.
    shared_scale : bool, default True
        Même échelle de couleur pour toutes les images (bornes communes,
        une seule barre de couleur) — pour comparer des niveaux. ``False`` :
        chaque image a ses propres bornes.
    vmin, vmax : float, optional
        Bornes imposées de l'échelle (prioritaires sur ``shared_scale``).
    title : str, optional
        Titre de la figure.
    panel_size : int, default 300
        Côté de chaque sous-graphe [px].

    Returns
    -------
    go.Figure

    Raises
    ------
    ValueError
        Si ``images`` est vide ou contient un tableau qui n'est pas 2D.
    """
    if not images:
        raise ValueError("images est vide.")
    for name, arr in images:
        if np.ndim(arr) != 2:
            raise ValueError(f"'{name}' : tableau 2D attendu, reçu ndim={np.ndim(arr)}.")

    n = len(images)
    ncols = ncols or min(n, 4)
    nrows = int(np.ceil(n / ncols))

    lo, hi = vmin, vmax
    if shared_scale:
        finite = [np.asarray(a)[np.isfinite(a)] for _, a in images]
        if lo is None:
            lo = float(min(f.min() for f in finite if f.size))
        if hi is None:
            hi = float(max(f.max() for f in finite if f.size))

    fig = make_subplots(
        rows=nrows,
        cols=ncols,
        subplot_titles=[name for name, _ in images],
        horizontal_spacing=0.02,
        vertical_spacing=0.06,
    )
    for i, (_, arr) in enumerate(images):
        row, col = divmod(i, ncols)
        fig.add_trace(
            go.Heatmap(
                z=np.asarray(arr),
                colorscale=cmap,
                zmin=lo,
                zmax=hi,
                showscale=shared_scale and i == 0,
                coloraxis=None,
            ),
            row=row + 1,
            col=col + 1,
        )

    for i in range(1, nrows * ncols + 1):
        suffix = "" if i == 1 else str(i)
        fig.layout[f"yaxis{suffix}"].update(
            autorange="reversed", scaleanchor=f"x{suffix}", scaleratio=1,
            showticklabels=False, showgrid=False, zeroline=False,
        )
        fig.layout[f"xaxis{suffix}"].update(
            showticklabels=False, showgrid=False, zeroline=False, constrain="domain",
        )
    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor="center"),
        width=panel_size * ncols + 80,
        height=panel_size * nrows + 60,
        margin=dict(l=0, r=0, t=60, b=0),
    )
    return fig
