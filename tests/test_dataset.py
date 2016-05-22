"""Test dataset module.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import numpy as np
from simretina import dataset

from nose.tools import assert_equal, assert_not_equal


def test_get_lenna():
    """Test dataset.get_lenna function."""
    lenna, size = dataset.get_lenna()

    assert_equal(lenna.shape, size)
    assert_not_equal(lenna, np.array([]))


def test_get_dog():
    """Test dataset.get_dog function."""
    dog, size = dataset.get_dog()

    assert_equal(dog.shape, size)
    assert_not_equal(dog, np.array([]))


def test_get_yuhuang():
    """Test dataset.get_yuhuang function."""
    yuhuang, size = dataset.get_yuhuang()

    assert_equal(yuhuang.shape, size)
    assert_not_equal(yuhuang, np.array([]))


def test_get_horse_riding():
    """Test dataset.get_horse_riding function."""
    horse_riding, size = dataset.get_horse_riding()

    assert_equal(horse_riding[0].shape, size)
    assert_not_equal(len(horse_riding), 0)


def test_get_taichi():
    """Test datset.get_taichi function."""
    taichi, size = dataset.get_taichi()

    assert_equal(taichi[0].shape, size)
    assert_not_equal(len(taichi), 0)
