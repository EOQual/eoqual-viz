"""Tests de `eoqual.viz.gallery.plot_image_grid` et `eoqual.viz.curves.plot_curves`."""

from __future__ import annotations

import numpy as np
import pytest

from eoqual.viz import plot_curves, plot_image_grid


def test_image_grid_layout_and_shared_scale():
    rng = np.random.default_rng(0)
    imgs = [(f"im{i}", rng.random((8, 10)) * (i + 1)) for i in range(5)]
    fig = plot_image_grid(imgs, ncols=3)
    assert len(fig.data) == 5
    assert all(t.type == "heatmap" for t in fig.data)
    lo = min(a.min() for _, a in imgs)
    assert all(t.zmin == pytest.approx(lo) for t in fig.data)
    assert sum(bool(t.showscale) for t in fig.data) == 1
    assert fig.layout.yaxis.autorange == "reversed"
    assert fig.layout.yaxis6.scaleanchor == "x6"


def test_image_grid_own_scale_and_errors():
    fig = plot_image_grid([("a", np.zeros((4, 4))), ("b", np.ones((4, 4)))], shared_scale=False)
    assert fig.data[0].zmin is None and not fig.data[0].showscale
    fig = plot_image_grid([("a", np.zeros((4, 4)))], vmin=-1, vmax=2)
    assert (fig.data[0].zmin, fig.data[0].zmax) == (-1, 2)
    with pytest.raises(ValueError):
        plot_image_grid([])
    with pytest.raises(ValueError):
        plot_image_grid([("cube", np.zeros((2, 2, 2)))])


def test_curves_log_axes_and_vlines():
    x = np.logspace(-3, 0, 10)
    fig = plot_curves([("a", x, x**2), ("b", x[:5], x[:5])], log_x=True, log_y=True,
                      markers=True, vlines=[(0.1, "opt", "red")])
    assert len(fig.data) == 2
    assert fig.data[0].mode == "lines+markers"
    assert fig.layout.xaxis.type == "log" and fig.layout.yaxis.type == "log"
    assert len(fig.layout.shapes) == 1
    with pytest.raises(ValueError):
        plot_curves([("bad", x, x[:3])])
    with pytest.raises(ValueError):
        plot_curves([])
