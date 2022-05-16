"""
Test Pearson module, pearson_2d function

Run with::

    python3 -m pytest test_pearson_2d.py
"""

import numpy as np

import pearson


def test_pearson_2d():
    # Test pearson_2d routine
    x = np.random.rand(22)
    Y = np.random.normal(size=(22, 12))
    # Does routine give same answers as np.corrcoef?
    expected = np.corrcoef(x, Y.T)[0, 1:]
    actual = pearson.pearson_2d(x, Y)
    # Did you, gentle user, forget to return the value?
    if actual is None:
        raise RuntimeError("function returned None")
    assert np.allclose(expected, actual)
