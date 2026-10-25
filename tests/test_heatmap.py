"""Tests de `eoqual.viz.heatmap.plot_array`."""

from __future__ import annotations

import numpy as np

from eoqual.viz.heatmap import plot_array


def test_plot_array_returns_single_heatmap_trace():
    arr = np.random.default_rng(0).random((16, 16))
    fig = plot_array(arr, title="test")
    assert len(fig.data) == 1
    assert fig.data[0].type == "heatmap"
    np.testing.assert_array_equal(fig.data[0].z, arr)


def test_plot_array_log_transforms_data():
    arr = np.full((8, 8), 100.0)
    fig = plot_array(arr, log=True)
    np.testing.assert_allclose(fig.data[0].z, np.log10(arr + 1e-12))


def test_plot_array_vmin_vmax_propagated():
    arr = np.random.default_rng(1).random((8, 8))
    fig = plot_array(arr, vmin=-1.0, vmax=1.0)
    assert fig.data[0].zmin == -1.0
    assert fig.data[0].zmax == 1.0


def test_plot_array_square_aspect_ratio():
    arr = np.zeros((8, 8))
    fig = plot_array(arr)
    assert fig.layout.yaxis.scaleanchor == "x"
    assert fig.layout.yaxis.scaleratio == 1
