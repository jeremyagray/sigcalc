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

from decimal import ROUND_CEILING
from decimal import ROUND_DOWN
from decimal import ROUND_FLOOR
from decimal import ROUND_HALF_DOWN
from decimal import ROUND_HALF_EVEN
from decimal import ROUND_HALF_UP
from decimal import ROUND_UP
from decimal import Decimal

import pytest

from sigcalc import Quantity
from sigcalc import _most_significant_place


# Helper function tests.
def test__most_significant_place():
    """Should return the power of the most significant place."""
    assert _most_significant_place(Decimal("31415926540")) == Decimal("10")
    assert _most_significant_place(Decimal("3141592654")) == Decimal("9")
    assert _most_significant_place(Decimal("314159265.4")) == Decimal("8")
    assert _most_significant_place(Decimal("31415926.54")) == Decimal("7")
    assert _most_significant_place(Decimal("3141592.654")) == Decimal("6")
    assert _most_significant_place(Decimal("314159.2654")) == Decimal("5")
    assert _most_significant_place(Decimal("31415.92654")) == Decimal("4")
    assert _most_significant_place(Decimal("3141.592654")) == Decimal("3")
    assert _most_significant_place(Decimal("314.1592654")) == Decimal("2")
    assert _most_significant_place(Decimal("31.41592654")) == Decimal("1")
    assert _most_significant_place(Decimal("3.141592654")) == Decimal("0")
    assert _most_significant_place(Decimal("0.3141592654")) == Decimal("-1")
    assert _most_significant_place(Decimal("0.03141592654")) == Decimal("-2")
    assert _most_significant_place(Decimal("0.003141592654")) == Decimal("-3")
    assert _most_significant_place(Decimal("0.0003141592654")) == Decimal("-4")
    assert _most_significant_place(Decimal("0.00003141592654")) == Decimal("-5")
    assert _most_significant_place(Decimal("0.000003141592654")) == Decimal("-6")
    assert _most_significant_place(Decimal("0.0000003141592654")) == Decimal("-7")
    assert _most_significant_place(Decimal("0.00000003141592654")) == Decimal("-8")
    assert _most_significant_place(Decimal("0.000000003141592654")) == Decimal("-9")
    assert _most_significant_place(Decimal("0.0000000003141592654")) == Decimal("-10")
    assert _most_significant_place(Decimal("-31415926540")) == Decimal("10")
    assert _most_significant_place(Decimal("-3141592654")) == Decimal("9")
    assert _most_significant_place(Decimal("-314159265.4")) == Decimal("8")
    assert _most_significant_place(Decimal("-31415926.54")) == Decimal("7")
    assert _most_significant_place(Decimal("-3141592.654")) == Decimal("6")
    assert _most_significant_place(Decimal("-314159.2654")) == Decimal("5")
    assert _most_significant_place(Decimal("-31415.92654")) == Decimal("4")
    assert _most_significant_place(Decimal("-3141.592654")) == Decimal("3")
    assert _most_significant_place(Decimal("-314.1592654")) == Decimal("2")
    assert _most_significant_place(Decimal("-31.41592654")) == Decimal("1")
    assert _most_significant_place(Decimal("-3.141592654")) == Decimal("0")
    assert _most_significant_place(Decimal("-0.3141592654")) == Decimal("-1")
    assert _most_significant_place(Decimal("-0.03141592654")) == Decimal("-2")
    assert _most_significant_place(Decimal("-0.003141592654")) == Decimal("-3")
    assert _most_significant_place(Decimal("-0.0003141592654")) == Decimal("-4")
    assert _most_significant_place(Decimal("-0.00003141592654")) == Decimal("-5")
    assert _most_significant_place(Decimal("-0.000003141592654")) == Decimal("-6")
    assert _most_significant_place(Decimal("-0.0000003141592654")) == Decimal("-7")
    assert _most_significant_place(Decimal("-0.00000003141592654")) == Decimal("-8")
    assert _most_significant_place(Decimal("-0.000000003141592654")) == Decimal("-9")
    assert _most_significant_place(Decimal("-0.0000000003141592654")) == Decimal("-10")


def test__most_significant_place_zero():
    """Should return zero as the most significant place for zero."""
    assert _most_significant_place(Decimal("0")) == Decimal("0")
    assert _most_significant_place(Decimal("0.000")) == Decimal("0")


# Output operations tests.
def test___repr__():
    """Should reproduce a ``Quantity`` object."""
    q = Quantity("3.14", "3")
    assert repr(q) == f'Quantity("{str(q.value)}", "{str(q.figures)}")'
    q = Quantity("3.14", "3", constant=True)
    assert repr(q) == f'Quantity("{str(q.value)}", "{str(q.figures)}", constant=True)'
    q = Quantity("3.14", "3", rounding=ROUND_HALF_EVEN)
    assert (
        repr(q)
        == f'Quantity("{str(q.value)}", "{str(q.figures)}", rounding=ROUND_HALF_EVEN)'
    )
    q = Quantity("3.14", "3", constant=True, rounding=ROUND_HALF_EVEN)
    assert repr(q) == (
        f'Quantity("{str(q.value)}", "{str(q.figures)}",'
        f" constant=True, rounding=ROUND_HALF_EVEN)"
    )


def test___format__():
    """Should format a ``Quantity`` object."""
    # Big numbers.
    q = Quantity("314", "1")
    assert f"{q:.0f}" == "300"
    assert f"{q:.0e}" == "3e+2"
    q = Quantity("314", "2")
    assert f"{q:.0f}" == "310"
    assert f"{q:.1e}" == "3.1e+2"
    q = Quantity("314", "3")
    assert f"{q:.0f}" == "314"
    assert f"{q:.2e}" == "3.14e+2"
    q = Quantity("314", "4")
    assert f"{q:.1f}" == "314.0"
    assert f"{q:.3e}" == "3.140e+2"

    q = Quantity("0.0314", "1")
    assert f"{q:.0e}" == "3e-2"
    q = Quantity("0.0314", "2")
    assert f"{q:.1e}" == "3.1e-2"
    q = Quantity("0.0314", "3")
    assert f"{q:.2e}" == "3.14e-2"
    q = Quantity("0.0314", "4")
    assert f"{q:.3e}" == "3.140e-2"


def test___str__():
    """Should stringify a ``Quantity`` object."""
    q = Quantity("3.14", "1", rounding=ROUND_HALF_UP)
    assert str(q) == "3"
    q = Quantity("3.14", "1", rounding=ROUND_HALF_DOWN)
    assert str(q) == "3"
    q = Quantity("3.14", "1", rounding=ROUND_HALF_EVEN)
    assert str(q) == "3"
    q = Quantity("3.14", "1", rounding=ROUND_CEILING)
    assert str(q) == "4"
    q = Quantity("3.14", "1", rounding=ROUND_FLOOR)
    assert str(q) == "3"
    q = Quantity("3.14", "1", rounding=ROUND_UP)
    assert str(q) == "4"
    q = Quantity("3.14", "1", rounding=ROUND_DOWN)
    assert str(q) == "3"

    q = Quantity("3.14", "2", rounding=ROUND_HALF_UP)
    assert str(q) == "3.1"
    q = Quantity("3.14", "2", rounding=ROUND_HALF_DOWN)
    assert str(q) == "3.1"
    q = Quantity("3.14", "2", rounding=ROUND_HALF_EVEN)
    assert str(q) == "3.1"
    q = Quantity("3.14", "2", rounding=ROUND_CEILING)
    assert str(q) == "3.2"
    q = Quantity("3.14", "2", rounding=ROUND_FLOOR)
    assert str(q) == "3.1"
    q = Quantity("3.14", "2", rounding=ROUND_UP)
    assert str(q) == "3.2"
    q = Quantity("3.14", "2", rounding=ROUND_DOWN)
    assert str(q) == "3.1"

    q = Quantity("3.14", "3", rounding=ROUND_HALF_UP)
    assert str(q) == "3.14"
    q = Quantity("3.14", "3", rounding=ROUND_HALF_DOWN)
    assert str(q) == "3.14"
    q = Quantity("3.14", "3", rounding=ROUND_HALF_EVEN)
    assert str(q) == "3.14"
    q = Quantity("3.14", "3", rounding=ROUND_CEILING)
    assert str(q) == "3.14"
    q = Quantity("3.14", "3", rounding=ROUND_FLOOR)
    assert str(q) == "3.14"
    q = Quantity("3.14", "3", rounding=ROUND_UP)
    assert str(q) == "3.14"
    q = Quantity("3.14", "3", rounding=ROUND_DOWN)
    assert str(q) == "3.14"

    q = Quantity("3.14", "4", rounding=ROUND_HALF_UP)
    assert str(q) == "3.140"
    q = Quantity("3.14", "4", rounding=ROUND_HALF_DOWN)
    assert str(q) == "3.140"
    q = Quantity("3.14", "4", rounding=ROUND_HALF_EVEN)
    assert str(q) == "3.140"
    q = Quantity("3.14", "4", rounding=ROUND_CEILING)
    assert str(q) == "3.140"
    q = Quantity("3.14", "4", rounding=ROUND_FLOOR)
    assert str(q) == "3.140"
    q = Quantity("3.14", "4", rounding=ROUND_UP)
    assert str(q) == "3.140"
    q = Quantity("3.14", "4", rounding=ROUND_DOWN)
    assert str(q) == "3.140"

    q = Quantity("3.145", "3", rounding=ROUND_HALF_UP)
    assert str(q) == "3.15"
    q = Quantity("3.145", "3", rounding=ROUND_HALF_DOWN)
    assert str(q) == "3.14"
    q = Quantity("3.145", "3", rounding=ROUND_HALF_EVEN)
    assert str(q) == "3.14"
    q = Quantity("3.145", "3", rounding=ROUND_CEILING)
    assert str(q) == "3.15"
    q = Quantity("3.145", "3", rounding=ROUND_FLOOR)
    assert str(q) == "3.14"
    q = Quantity("3.145", "3", rounding=ROUND_UP)
    assert str(q) == "3.15"
    q = Quantity("3.145", "3", rounding=ROUND_DOWN)
    assert str(q) == "3.14"

    q = Quantity("3.135", "3", rounding=ROUND_HALF_UP)
    assert str(q) == "3.14"
    q = Quantity("3.135", "3", rounding=ROUND_HALF_DOWN)
    assert str(q) == "3.13"
    q = Quantity("3.135", "3", rounding=ROUND_HALF_EVEN)
    assert str(q) == "3.14"
    q = Quantity("3.135", "3", rounding=ROUND_CEILING)
    assert str(q) == "3.14"
    q = Quantity("3.135", "3", rounding=ROUND_FLOOR)
    assert str(q) == "3.13"
    q = Quantity("3.135", "3", rounding=ROUND_UP)
    assert str(q) == "3.14"
    q = Quantity("3.135", "3", rounding=ROUND_DOWN)
    assert str(q) == "3.13"

    q = Quantity("-3.135", "3", rounding=ROUND_HALF_UP)
    assert str(q) == "-3.14"
    q = Quantity("-3.135", "3", rounding=ROUND_HALF_DOWN)
    assert str(q) == "-3.13"
    q = Quantity("-3.135", "3", rounding=ROUND_HALF_EVEN)
    assert str(q) == "-3.14"
    q = Quantity("-3.135", "3", rounding=ROUND_CEILING)
    assert str(q) == "-3.13"
    q = Quantity("-3.135", "3", rounding=ROUND_FLOOR)
    assert str(q) == "-3.14"
    q = Quantity("-3.135", "3", rounding=ROUND_UP)
    assert str(q) == "-3.14"
    q = Quantity("-3.135", "3", rounding=ROUND_DOWN)
    assert str(q) == "-3.13"


def test__round_constants():
    """Constants should not round."""
    q = Quantity("3.14", "2", constant=True)
    assert q._round() == Decimal("3.14")


def test_round_constants():
    """Constants should not round."""
    q = Quantity("3.14", "2", constant=True)
    assert q.round() == q


def test_round():
    """Should round a ``Quantity`` object."""
    q = Quantity("3.14", "2")
    assert q.round() == Quantity("3.1", "2")


# Unary operations tests.
def test_abs():
    """Should return the absolute value of a ``Quantity`` object."""
    assert abs(Quantity("3.14", "3")) == Quantity("3.14", "3")
    assert abs(Quantity("-3.14", "3")) == Quantity("3.14", "3")
    assert abs(Quantity("+3.14", "3")) == Quantity("3.14", "3")
    assert abs(Quantity("0", "3")) == Quantity("0", "3")
    assert abs(Quantity("-0", "3")) == Quantity("0", "3")
    assert abs(Quantity("+0", "3")) == Quantity("0", "3")
    # Constants.
    assert abs(Quantity("3.14", "3", constant=True)) == Quantity(
        "3.14", "3", constant=True
    )


def test_neg():
    """Should return the negation of a ``Quantity`` object."""
    assert -Quantity("3.14", "3") == Quantity("-3.14", "3")
    assert -Quantity("-3.14", "3") == Quantity("3.14", "3")
    assert -Quantity("+3.14", "3") == Quantity("-3.14", "3")
    assert -Quantity("0", "3") == Quantity("-0", "3")
    assert -Quantity("-0", "3") == Quantity("0", "3")
    assert -Quantity("+0", "3") == Quantity("0", "3")
    # Constants.
    assert -Quantity("3.14", "3", constant=True) == Quantity(
        "-3.14", "3", constant=True
    )


def test_pos():
    """Should return the positive of a ``Quantity`` object."""
    assert +Quantity("3.14", "3") == Quantity("3.14", "3")
    assert +Quantity("-3.14", "3") == Quantity("-3.14", "3")
    assert +Quantity("+3.14", "3") == Quantity("3.14", "3")
    assert +Quantity("0", "3") == Quantity("0", "3")
    assert +Quantity("-0", "3") == Quantity("0", "3")
    assert +Quantity("+0", "3") == Quantity("0", "3")
    # Constants.
    assert +Quantity("3.14", "3", constant=True) == Quantity("3.14", "3", constant=True)


# Comparisons tests.
def test_equal():
    """Equal ``Quantity`` objects should be equal."""
    assert Quantity("3.14", "3") == Quantity("3.14", "3")
    assert Quantity("3.140", "3") == Quantity("3.14", "3")
    assert Quantity("3.14", "3") == Quantity("3.140", "3")
    # Constants.
    assert Quantity("3.14", "3", constant=True) == Quantity("3.14", "3", constant=True)


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
    # Constants.
    assert Quantity("3.14", "3", constant=True) != Quantity("3.14", "3")
    assert Quantity("3.14", "3") != Quantity("3.14", "3", constant=True)


# Arithmetic operations tests.
def test_add():
    """Quantities should add."""
    assert Quantity("3.14", "3") + Quantity("2.72", "3") == Quantity("5.86", "3")
    assert Quantity("3.14", "3") + Quantity("0.272", "3") == Quantity("3.412", "3")
    assert Quantity("100", "1") + Quantity("0.001", "1") == Quantity("100.001", "1")
    assert Quantity("100", "3") + Quantity("0.001", "1") == Quantity("100.001", "3")
    assert Quantity("100.0", "4") + Quantity("0.001", "1") == Quantity("100.001", "4")
    # Exponents.
    assert Quantity("3.14e-8", "3") + Quantity("2.72e-8", "3") == Quantity(
        "5.86e-8", "3"
    )
    assert Quantity("3.14e8", "3") + Quantity("2.72e8", "3") == Quantity("5.86e8", "3")
    # Constants.
    assert Quantity("3.1415", "5") + Quantity("2.72", "3", constant=True) == Quantity(
        "5.8615", "5"
    )
    assert Quantity("3.1415", "5", constant=True) + Quantity("2.72", "3") == Quantity(
        "5.8615", "3"
    )
    assert Quantity("3.1415", "5", constant=True) + Quantity(
        "2.72", "3", constant=True
    ) == Quantity("5.8615", "5", constant=True)


def test_add_bad_types():
    """Only quantities should add."""
    with pytest.raises(TypeError):
        Quantity("3.14", "3") + 3
    with pytest.raises(TypeError):
        3 + Quantity("3.14", "3")


def test_sub():
    """Quantities should subtract."""
    # Easy.
    assert Quantity("3.14", "3") - Quantity("1.72", "3") == Quantity("1.42", "3")
    # Loss of precision.
    assert Quantity("3.14", "3") - Quantity("2.72", "3") == Quantity("0.42", "2")
    # First subtrahend more precise.
    assert Quantity("3.1415", "5") - Quantity("2.72", "3") == Quantity("0.4215", "2")
    assert Quantity("3.1415", "5") - Quantity("0.272", "3") == Quantity("2.8695", "4")
    # Second subtrahend more precise.
    assert Quantity("3.14", "3") - Quantity("0.272", "3") == Quantity("2.868", "3")
    # No overlap between subtrahends.
    assert Quantity("3.14", "3") - Quantity("0.00272", "3") == Quantity("3.13728", "3")
    # Rounding regains precision.
    assert Quantity("100", "1") - Quantity("0.001", "1") == Quantity("99.999", "1")
    assert Quantity("100", "1") - Quantity("0.005", "1") == Quantity("99.995", "1")
    assert Quantity("100", "1") - Quantity("0.006", "1") == Quantity("99.994", "1")
    assert Quantity("100.0", "4") - Quantity("0.001", "1") == Quantity("99.999", "4")
    # Constants.
    assert Quantity("3.1415", "5") - Quantity("1.12", "3", constant=True) == Quantity(
        "2.0215", "5"
    )
    assert Quantity("3.1415", "5", constant=True) - Quantity("1.12", "3") == Quantity(
        "2.0215", "3"
    )
    assert Quantity("3.1415", "5", constant=True) - Quantity(
        "1.12", "3", constant=True
    ) == Quantity("2.0215", "4", constant=True)
    assert Quantity("3.1415", "5") - Quantity("2.72", "3", constant=True) == Quantity(
        "0.4215", "4"
    )
    assert Quantity("3.1415", "5", constant=True) - Quantity("2.72", "3") == Quantity(
        "0.4215", "2"
    )
    assert Quantity("3.1415", "5", constant=True) - Quantity(
        "2.72", "3", constant=True
    ) == Quantity("0.4215", "4", constant=True)


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
    # Constants.
    assert Quantity("3.1415", "5") * Quantity("2.72", "3", constant=True) == Quantity(
        "8.54488", "5"
    )
    assert Quantity("2.72", "3", constant=True) * Quantity("3.1415", "5") == Quantity(
        "8.54488", "5"
    )
    assert Quantity("2.72", "3", constant=True) * Quantity(
        "3.1415", "5", constant=True
    ) == Quantity("8.54488", "5", constant=True)


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
    # Constants.
    assert Quantity("3.1415", "5") / Quantity("2.72", "3", constant=True) == Quantity(
        "1.154963235294117647058823529", "5"
    )
    assert Quantity("3.1415", "5", constant=True) / Quantity("2.72", "3") == Quantity(
        "1.154963235294117647058823529", "3"
    )
    assert Quantity("3.1415", "5", constant=True) / Quantity(
        "2.72", "3", constant=True
    ) == Quantity("1.154963235294117647058823529", "3", constant=True)


def test_div_bad_types():
    """Only quantities should divide."""
    with pytest.raises(TypeError):
        Quantity("3.14", "3") / 3
    with pytest.raises(TypeError):
        3 / Quantity("3.14", "3")


def test_textbook_examples():
    """Should corroborate answers to textbook problems."""
    # holt:chemistry2006
    # Sample Problem A and Practice, p. 59.
    # Note that source has a mistake due to rounding before the end of
    # the calculation.
    assert (Quantity("36.79", "4") - Quantity("21.6", "3")) / Quantity(
        "23.62", "4"
    ) == Quantity("0.6430990685859441151566469094", "3")
    assert Quantity("0.1273", "4") - Quantity("0.000008", "1") == Quantity(
        "0.127292", "4"
    )
    assert (Quantity("12.4", "3") * Quantity("7.943", "4")) + Quantity(
        "0.0064", "2"
    ) == Quantity("98.4996", "3")
    assert (Quantity("246.83", "5") / Quantity("26", "5", constant=True)) - Quantity(
        "1.349", "4"
    ) == Quantity("8.144461538461538461538461538", "4")
    assert (Quantity("215.6", "4") - Quantity("110.4", "4")) / Quantity(
        "114", "3"
    ) == Quantity("0.9228070175438596491228070175", "3")
    assert Quantity("653550", "5") / Quantity("142.3", "4") == Quantity(
        "4592.761770906535488404778637", "4"
    )


def test_constant():
    """Constant ``Quantity`` objects should return ``True``."""
    q = Quantity("3.14", "3")
    assert q.constant is False
    q = Quantity("3.14", "3", constant=False)
    assert q.constant is False
    q = Quantity("3.14", "3", constant=True)
    assert q.constant is True


def test_modify_constant():
    """Should create and return constant ``Quantity`` objects."""
    q = Quantity("3.14", "3")
    q.constant = True
    assert q.constant is True
    q.constant = False
    assert q.constant is False
    q.constant = "howdy"
    assert q.constant is False


def test_create_constant_idempotent():
    """Should create and return constant ``Quantity`` objects."""
    q = Quantity("3.14", "3")
    q.constant = True
    q.constant = True
    assert q.constant is True

    r = Quantity("3.14", "3")
    assert r.constant is False
    r.constant = False
    r.constant = False
    assert r.constant is False
