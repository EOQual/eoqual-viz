#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualisation interactive d'un tableau 2D (Plotly).
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import plotly.graph_objects as go


def plot_array(
    arr: np.ndarray,
    *,
    title: str = "",
    cmap: str = "viridis",
    log: bool = False,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
    cbar_label: str = "",
) -> go.Figure:
    """
    Visualisation interactive d'un tableau 2D avec Plotly (heatmap).

    Parameters
    ----------
    arr : np.ndarray
        Tableau à afficher (2D).
    title : str, optional
        Titre du graphique.
    cmap : str, default "viridis"
        Nom du colormap Plotly (voir https://plotly.com/python/builtin-colorscales/).
    log : bool, default False
        Si ``True`` on trace ``log10(arr)`` — pratique pour une PSF
        (dynamique large, des ordres de grandeur entre le pic et les ailes).
    vmin, vmax : float, optional
        Limites de l'échelle de couleur.
    cbar_label : str, optional
        Légende de la barre de couleur.

    Returns
    -------
    go.Figure
        Figure Plotly prête à être affichée avec ``fig.show()``.
    """
    data = np.log10(arr + 1e-12) if log else arr

    fig = go.Figure(
        data=go.Heatmap(
            z=data,
            colorscale=cmap,
            zmin=vmin,
            zmax=vmax,
            colorbar=dict(title=cbar_label) if cbar_label else None,
            showscale=True,
        )
    )
    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor="center"),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            constrain="domain",
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            scaleanchor="x",
            scaleratio=1,
        ),
        width=500,
        height=500,
        margin=dict(l=0, r=0, t=30, b=0),
    )

    return fig
