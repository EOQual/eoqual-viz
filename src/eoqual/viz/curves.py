#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plusieurs courbes sur un même graphe (Plotly), axes linéaires ou
logarithmiques, avec repères optionnels.
"""

from __future__ import annotations

from typing import Optional, Sequence, Tuple

import numpy as np
import plotly.graph_objects as go


def plot_curves(
    curves: Sequence[Tuple[str, np.ndarray, np.ndarray]],
    *,
    log_x: bool = False,
    log_y: bool = False,
    markers: bool = False,
    vlines: Optional[Sequence[Tuple[float, str, str]]] = None,
    xlabel: str = "",
    ylabel: str = "",
    title: str = "",
    width: int = 700,
    height: int = 420,
) -> go.Figure:
    """
    Trace une ou plusieurs courbes ``y(x)`` sur un même graphe — par
    exemple une valeur au fil des itérations, ou un critère en fonction
    d'un paramètre.

    Parameters
    ----------
    curves : sequence of (str, NDArray, NDArray)
        ``(étiquette, x, y)`` par courbe. Chaque courbe a son propre ``x``.
    log_x, log_y : bool, default False
        Échelle logarithmique de l'axe.
    markers : bool, default False
        Ajoute un marqueur à chaque point.
    vlines : sequence of (float, str, str), optional
        Repères verticaux ``(valeur, étiquette, couleur)``.
    xlabel, ylabel, title : str, optional
        Légendes des axes et titre.
    width, height : int
        Taille de la figure [px].

    Returns
    -------
    go.Figure

    Raises
    ------
    ValueError
        Si ``curves`` est vide, ou si ``x`` et ``y`` d'une courbe n'ont pas
        la même longueur.
    """
    if not curves:
        raise ValueError("curves est vide.")
    fig = go.Figure()
    mode = "lines+markers" if markers else "lines"
    for label, x, y in curves:
        if len(x) != len(y):
            raise ValueError(f"'{label}' : x ({len(x)}) et y ({len(y)}) de longueurs différentes.")
        fig.add_scatter(x=np.asarray(x), y=np.asarray(y), name=label, mode=mode)
    for value, label, color in vlines or ():
        fig.add_vline(
            x=value, line=dict(color=color, dash="dot"),
            annotation_text=label, annotation_position="top",
        )
    fig.update_xaxes(title_text=xlabel, type="log" if log_x else "linear")
    fig.update_yaxes(title_text=ylabel, type="log" if log_y else "linear")
    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor="center"),
        width=width,
        height=height,
        margin=dict(l=0, r=0, t=60, b=0),
    )
    return fig
