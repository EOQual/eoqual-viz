"""Tests de `eoqual.viz.profile.plot_curve_grid`."""

from __future__ import annotations

import numpy as np
import pytest

from eoqual.viz.profile import plot_curve_grid


def test_single_panel_estimated_only():
    x = np.linspace(-1, 1, 21)
    y = x ** 2
    fig = plot_curve_grid(x, [("Parabole", y)])
    assert len(fig.data) == 1
    np.testing.assert_array_equal(fig.data[0].x, x)
    np.testing.assert_array_equal(fig.data[0].y, y)


def test_two_panels_with_partial_reference():
    x = np.linspace(0, 1, 11)
    y1, y2 = x, x ** 2
    ref1 = x + 0.1
    fig = plot_curve_grid(
        x, [("A", y1), ("B", y2)], references=[ref1, None],
    )
    # 2 estimées + 1 seule référence (B n'en a pas) = 3 traces.
    assert len(fig.data) == 3


def test_references_length_mismatch_raises():
    x = np.linspace(0, 1, 5)
    with pytest.raises(ValueError):
        plot_curve_grid(x, [("A", x), ("B", x)], references=[x])


def test_vlines_applied_to_every_panel():
    x = np.linspace(0, 2, 5)
    fig = plot_curve_grid(
        x, [("A", x), ("B", x), ("C", x)],
        vlines=[(1.0, "fc", "red"), (0.5, "autre", "blue")],
    )
    vlines = [shape for shape in fig.layout.shapes if shape.type == "line"]
    # 2 repères x 3 sous-graphes.
    assert len(vlines) == 6
    assert {shape.line.color for shape in vlines} == {"red", "blue"}


def test_x_range_and_y_range_propagated_to_every_axis():
    x = np.linspace(0, 1, 5)
    fig = plot_curve_grid(
        x, [("A", x), ("B", x)], x_range=(0, 3), y_range=(-2, 2),
    )
    for axis_name in ("xaxis", "xaxis2"):
        assert list(fig.layout[axis_name].range) == [0, 3]
    for axis_name in ("yaxis", "yaxis2"):
        assert list(fig.layout[axis_name].range) == [-2, 2]


def test_estimated_legend_shown_once_not_per_panel():
    x = np.linspace(0, 1, 5)
    fig = plot_curve_grid(x, [("A", x), ("B", x)], references=[x, x])
    showlegend_flags = [trace.showlegend for trace in fig.data]
    # 4 traces (2 panels x estimée+référence) ; une seule paire doit
    # porter la légende (showlegend=True), l'autre non -- sinon la
    # légende de la figure affiche des entrées en double.
    assert showlegend_flags.count(True) == 2
    assert showlegend_flags.count(False) == 2
