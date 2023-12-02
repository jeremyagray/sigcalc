# ******************************************************************************
#
# sigcalc, significant figures calculations
#
# Copyright 2023 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""Quantity class tests."""

import pytest

from sigcalc import Quantity

# Output operations tests.


# Unary operations tests.
def test_abs():
    """Should return the absolute value of a ``Quantity`` object."""
    assert abs(Quantity("3.14", "3")) == Quantity("3.14", "3")
    assert abs(Quantity("-3.14", "3")) == Quantity("3.14", "3")
    assert abs(Quantity("+3.14", "3")) == Quantity("3.14", "3")
    assert abs(Quantity("0", "3")) == Quantity("0", "3")
    assert abs(Quantity("-0", "3")) == Quantity("0", "3")
    assert abs(Quantity("+0", "3")) == Quantity("0", "3")


def test_neg():
    """Should return the negation of a ``Quantity`` object."""
    assert -Quantity("3.14", "3") == Quantity("-3.14", "3")
    assert -Quantity("-3.14", "3") == Quantity("3.14", "3")
    assert -Quantity("+3.14", "3") == Quantity("-3.14", "3")
    assert -Quantity("0", "3") == Quantity("-0", "3")
    assert -Quantity("-0", "3") == Quantity("0", "3")
    assert -Quantity("+0", "3") == Quantity("0", "3")


def test_pos():
    """Should return the positive of a ``Quantity`` object."""
    assert +Quantity("3.14", "3") == Quantity("3.14", "3")
    assert +Quantity("-3.14", "3") == Quantity("-3.14", "3")
    assert +Quantity("+3.14", "3") == Quantity("3.14", "3")
    assert +Quantity("0", "3") == Quantity("0", "3")
    assert +Quantity("-0", "3") == Quantity("0", "3")
    assert +Quantity("+0", "3") == Quantity("0", "3")


# Comparisons tests.
def test_equal():
    """Equal ``Quantity`` objects should be equal."""
    assert Quantity("3.14", "3") == Quantity("3.14", "3")
    assert Quantity("3.140", "3") == Quantity("3.14", "3")
    assert Quantity("3.14", "3") == Quantity("3.140", "3")


def test_not_equal():
    """Unequal ``Quantity`` objects should not be equal."""
    assert Quantity("3.14", "3") != Quantity("3.14", "2")
    assert Quantity("3.14", "3") != Quantity("3.14", "4")

    assert Quantity("3.14", "3") != Quantity("3.15", "2")
    assert Quantity("3.14", "3") != Quantity("3.15", "3")
    assert Quantity("3.14", "3") != Quantity("3.15", "4")

    assert Quantity("3.14", "3") != Quantity("3.13", "2")
    assert Quantity("3.14", "3") != Quantity("3.13", "3")
    assert Quantity("3.14", "3") != Quantity("3.13", "4")


# Arithmetic operations tests.
def test_add():
    """Quantities should add."""
    assert Quantity("3.14", "3") + Quantity("2.72", "3") == Quantity("5.86", "3")
    assert Quantity("3.14", "3") + Quantity("0.272", "3") == Quantity("3.41", "3")


def test_add_bad_types():
    """Only quantities should add."""
    with pytest.raises(TypeError):
        Quantity("3.14", "3") + 3
    with pytest.raises(TypeError):
        3 + Quantity("3.14", "3")


def test_sub():
    """Quantities should subtract."""
    assert Quantity("3.14", "3") - Quantity("2.72", "3") == Quantity("0.42", "2")
    assert Quantity("3.14", "3") - Quantity("0.272", "3") == Quantity("2.868", "3")


def test_sub_bad_types():
    """Only quantities should subtract."""
    with pytest.raises(TypeError):
        Quantity("3.14", "3") - 3
    with pytest.raises(TypeError):
        3 - Quantity("3.14", "3")


def test_mult():
    """Quantities should multiply."""
    # 3.14 * 2.72 = 8.5408
    assert Quantity("3.14", "3") * Quantity("2.72", "3") == Quantity("8.5408", "3")
    assert Quantity("3.14", "3") * Quantity("0.272", "3") == Quantity("0.85408", "3")
    assert Quantity("3.14", "3") * Quantity("0.0272", "3") == Quantity("0.085408", "3")
    assert Quantity("314", "3") * Quantity("272", "3") == Quantity("85408", "3")
    assert Quantity("3140", "3") * Quantity("2720", "3") == Quantity("8540800", "3")
    assert Quantity("0.00314", "3") * Quantity("0.00272", "3") == Quantity(
        "0.0000085408", "3"
    )


def test_mul_bad_types():
    """Only quantities should multiply."""
    with pytest.raises(TypeError):
        Quantity("3.14", "3") * 3
    with pytest.raises(TypeError):
        3 * Quantity("3.14", "3")


def test_div():
    """Quantities should divide."""
    # 8.5408 / 2.72 = 3.14
    assert Quantity("8.5408", "3") / Quantity("2.72", "3") == Quantity("3.14", "3")
    assert Quantity("8.5408", "3") / Quantity("0.272", "3") == Quantity("31.4", "3")
    assert Quantity("8.5408", "3") / Quantity("0.0272", "3") == Quantity("314", "3")
    assert Quantity("85408", "3") / Quantity("272", "3") == Quantity("314", "3")
    assert Quantity("854080", "3") / Quantity("2720", "3") == Quantity("314", "3")
    assert Quantity("0.0085408", "3") / Quantity("0.00272", "3") == Quantity(
        "3.14", "3"
    )
    assert Quantity("0.85408", "3") / Quantity("2.72", "3") == Quantity("0.314", "3")
    assert Quantity("0.085408", "3") / Quantity("2.72", "3") == Quantity("0.0314", "3")
    assert Quantity("0.0085408", "3") / Quantity("2.72", "3") == Quantity(
        "0.00314", "3"
    )


def test_div_bad_types():
    """Only quantities should divide."""
    with pytest.raises(TypeError):
        Quantity("3.14", "3") / 3
    with pytest.raises(TypeError):
        3 / Quantity("3.14", "3")
