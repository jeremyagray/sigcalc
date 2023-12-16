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

"""Quantity hypothesis tests."""

from decimal import ROUND_05UP
from decimal import ROUND_CEILING
from decimal import ROUND_DOWN
from decimal import ROUND_FLOOR
from decimal import ROUND_HALF_DOWN
from decimal import ROUND_HALF_EVEN
from decimal import ROUND_HALF_UP
from decimal import ROUND_UP
from decimal import Decimal
from decimal import getcontext

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from sigcalc import Quantity


@composite
def quantities(draw):
    """Generate quantities."""
    return Quantity(
        draw(
            st.decimals(
                allow_nan=False,
                allow_infinity=False,
            )
        ),
        draw(
            st.integers(
                min_value=1,
                max_value=100,
            )
        ),
        draw(st.booleans()),
    )


@composite
def rounding(draw):
    """Generate a rounding mode."""
    return draw(
        st.sampled_from(
            [
                ROUND_CEILING,
                ROUND_DOWN,
                ROUND_FLOOR,
                ROUND_HALF_DOWN,
                ROUND_HALF_EVEN,
                ROUND_HALF_UP,
                ROUND_UP,
                ROUND_05UP,
            ]
        )
    )


@given(quantities(), rounding())
def test_equality_hypothesis(q, r):
    """Should order ``Quantity`` objects."""
    getcontext().rounding = r
    assert q == q
    assert not q != q


@given(quantities(), rounding())
def test_equality_different_precision_hypothesis(q, r):
    """Should order ``Quantity`` objects."""
    getcontext().rounding = r
    if q.figures == getcontext().prec:
        p = Quantity(q.value, q.figures - Decimal("1"), False)
    else:
        p = Quantity(q.value, q.figures + Decimal("1"), q.constant)

    assert q != p


@given(quantities(), rounding())
def test_abs_hypothesis(q, r):
    """Should calculate absolute value of ``Quantity`` objects."""
    getcontext().rounding = r
    p = Quantity(abs(q.value), q.figures, q.constant)
    assert abs(q) == p
    assert abs(abs(q)) == p


@given(quantities(), rounding())
def test_neg_hypothesis(q, r):
    """Should negate ``Quantity`` objects."""
    getcontext().rounding = r
    assert -(-q) == q


@given(quantities(), rounding())
def test_pos_hypothesis(q, r):
    """Should return ``Quantity`` objects."""
    getcontext().rounding = r
    p = Quantity(q.value, q.figures, q.constant)
    assert +q == q
    assert ++q == q
    assert +q == p


@given(quantities(), rounding())
def test_round_hypothesis(q, r):
    """Should round ``Quantity`` objects."""
    getcontext().rounding = r
    assert q.round() == q.round().round()


# Fails due to jeremyagray/sigcalc#23.
# @given(quantities(), rounding())
# def test_additive_identity_hypothesis(q, r):
#     """``Quantity`` objects should have an additive identity."""
#     getcontext().rounding = r
#     id = Quantity("0", "1", True)
#     assert q + id == q
#     assert id + q == q
#     assert id + q + id == q


# Fails due to jeremyagray/sigcalc#23.
# @given(quantities(), rounding())
# def test_subtractive_identity_hypothesis(q, r):
#     """``Quantity`` objects should have a subtractive identity."""
#     getcontext().rounding = r
#     id = Quantity("0", "1", True)
#     assert q - id == q


@given(quantities(), rounding())
def test_multiplicative_identity_hypothesis(q, r):
    """``Quantity`` objects should have a multiplicative identity."""
    getcontext().rounding = r
    id = Quantity("1", "1", True)
    assert q * id == q
    assert id * q == q
    assert id * q * id == q


@given(quantities(), rounding())
def test_divisive_identity_hypothesis(q, r):
    """``Quantity`` objects should have a divisive identity."""
    getcontext().rounding = r
    id = Quantity("1", "1", True)
    assert q / id == q
