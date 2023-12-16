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
        draw(
            st.sampled_from(
                [
                    ROUND_CEILING,
                    ROUND_DOWN,
                    ROUND_FLOOR,
                    ROUND_HALF_DOWN,
                    ROUND_HALF_EVEN,
                    ROUND_HALF_UP,
                    ROUND_UP,
                ]
            )
        ),
    )


@given(quantities())
def test_equality_hypothesis(q):
    """Should order ``Quantity`` objects."""
    assert q == q
    assert not q != q


@given(quantities())
def test_equality_different_precision_hypothesis(q):
    """Should order ``Quantity`` objects."""
    if q.figures == getcontext().prec:
        r = Quantity(q.value, q.figures - Decimal("1"), False, q.rounding)
    else:
        r = Quantity(q.value, q.figures + Decimal("1"), q.constant, q.rounding)

    assert q != r


@given(quantities())
def test_abs_hypothesis(q):
    """Should calculate absolute value of ``Quantity`` objects."""
    r = Quantity(abs(q.value), q.figures, q.constant, q.rounding)
    assert abs(q) == r
    assert abs(abs(q)) == r


@given(quantities())
def test_neg_hypothesis(q):
    """Should negate ``Quantity`` objects."""
    assert -(-q) == q


@given(quantities())
def test_pos_hypothesis(q):
    """Should return ``Quantity`` objects."""
    r = Quantity(q.value, q.figures, q.constant, q.rounding)
    assert +q == q
    assert ++q == q
    assert +q == r


@given(quantities())
def test_round_hypothesis(q):
    """Should round ``Quantity`` objects."""
    assert q.round() == q.round().round()
