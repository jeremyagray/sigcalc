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

import math
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

from hypothesis import assume
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
    assert q <= q
    assert q >= q
    assert not q != q


@given(quantities(), rounding())
def test_ordering_hypothesis(q, r):
    """Should order ``Quantity`` objects."""
    # Zeroes satisfy equality.
    assume(q.value != 0)
    getcontext().rounding = r
    assert q + abs(q) > q
    assert q > q - abs(q)
    assert q < q + abs(q)
    assert q - abs(q) < q


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


@given(quantities(), rounding())
def test_additive_identity_hypothesis(q, r):
    """``Quantity`` objects should have an additive identity."""
    getcontext().rounding = r
    id = Quantity("0", "1", True)
    assert q + id == q
    assert id + q == q
    assert id + q + id == q


@given(quantities(), rounding())
def test_subtractive_identity_hypothesis(q, r):
    """``Quantity`` objects should have a subtractive identity."""
    getcontext().rounding = r
    id = Quantity("0", "1", True)
    assert q - id == q


@given(quantities(), rounding())
def test_additive_inverse_hypothesis(q, r):
    """``Quantity`` objects should have an additive inverse."""
    getcontext().rounding = r
    # assert q - q == Quantity("0", q.figures, q.constant)
    assert q + q - q == q
    assert q - q + q == q


@given(quantities(), rounding())
def test_multiplicative_identity_hypothesis(q, r):
    """``Quantity`` objects should have a multiplicative identity."""
    getcontext().rounding = r
    id = Quantity("1", "1", True)
    assert q * id == q
    assert id * q == q
    assert id * q * id == q

    id = Quantity("1", q.figures)
    assert q * id == q
    assert id * q == q
    assert id * q * id == q


@given(quantities(), rounding())
def test_divisive_identity_hypothesis(q, r):
    """``Quantity`` objects should have a divisive identity."""
    getcontext().rounding = r
    id = Quantity("1", "1", True)
    assert q / id == q

    id = Quantity("1", q.figures)
    assert q / id == q


@given(quantities(), rounding(), st.booleans())
def test_constant_setter_hypothesis(q, r, c):
    """Should set the ``constant`` attribute."""
    getcontext().rounding = r
    q.constant = c
    assert q.constant is c


# Exponential function tests.
@given(quantities(), rounding())
def test_exp_hypothesis(q, r):
    """Should calculate the exponential of ``Quantity`` objects."""
    # Avoid decimal overflow.
    assume(q.value < Decimal("2302586"))

    getcontext().rounding = r
    e = q.exp()

    assert q.value.exp() == e.value
    assert q.figures == e.figures
    assert q.constant == e.constant


@given(quantities(), rounding())
def test_sqrt_hypothesis(q, r):
    """Should calculate the square root of ``Quantity`` objects."""
    # Avoid domain problems.
    assume(q.value > Decimal("0"))

    getcontext().rounding = r
    e = q.sqrt()

    assert q.value.sqrt() == e.value
    assert q.figures == e.figures
    assert q.constant == e.constant


# Logarithmic function tests.
@given(quantities(), rounding())
def test_ln_hypothesis(q, r):
    """Should calculate the natural logarithm of ``Quantity`` objects."""
    # Avoid logarithm domain problems.
    assume(q.value > Decimal("0"))
    assume(not math.isnan(q.value))

    getcontext().rounding = r
    e = q.ln()

    # Calculate significant figures.
    if abs(q.value) >= Decimal("1").exp() or abs(q.value) <= Decimal("-1").exp():
        # Include abscissa digits for values -1 <= x <= 1.
        a = math.floor(math.log10(math.floor(abs(e.value)))) + 1
    else:
        # No abscissa digits.
        a = 0

    assert q.value.ln() == e.value
    assert q.figures + a == e.figures
    assert q.constant == e.constant


@given(quantities(), rounding())
def test_log10_hypothesis(q, r):
    """Should calculate the base 10 logarithm of ``Quantity`` objects."""
    # Avoid logarithm domain problems.
    assume(q.value > Decimal("0"))
    assume(not math.isnan(q.value))

    getcontext().rounding = r
    e = q.log10()

    # Calculate significant figures.
    if abs(q.value) >= Decimal("10") or abs(q.value) <= Decimal("0.1"):
        # Include abscissa digits for values -1 <= x <= 1.
        a = math.floor(math.log10(math.floor(abs(e.value)))) + 1
    else:
        # No abscissa digits.
        a = 0

    assert q.value.log10() == e.value
    assert q.figures + a == e.figures
    assert q.constant == e.constant


# Trigonometric function tests.
@given(quantities(), rounding())
def test_sin_hypothesis(q, r):
    """Should calculate the sine of ``Quantity`` objects."""
    assert q.sin() == NotImplemented


@given(quantities(), rounding())
def test_asin_hypothesis(q, r):
    """Should calculate the inverse sine of ``Quantity`` objects."""
    assert q.asin() == NotImplemented


@given(quantities(), rounding())
def test_cos_hypothesis(q, r):
    """Should calculate the cosine of ``Quantity`` objects."""
    assert q.cos() == NotImplemented


@given(quantities(), rounding())
def test_acos_hypothesis(q, r):
    """Should calculate the inverse cosine of ``Quantity`` objects."""
    assert q.acos() == NotImplemented


@given(quantities(), rounding())
def test_tan_hypothesis(q, r):
    """Should calculate the tangent of ``Quantity`` objects."""
    assert q.tan() == NotImplemented


@given(quantities(), rounding())
def test_atan_hypothesis(q, r):
    """Should calculate the inverse tangent of ``Quantity`` objects."""
    assert q.atan() == NotImplemented


@given(quantities(), rounding())
def test_csc_hypothesis(q, r):
    """Should calculate the cosecant of ``Quantity`` objects."""
    assert q.csc() == NotImplemented


@given(quantities(), rounding())
def test_acsc_hypothesis(q, r):
    """Should calculate the inverse cosecant of ``Quantity`` objects."""
    assert q.acsc() == NotImplemented


@given(quantities(), rounding())
def test_sec_hypothesis(q, r):
    """Should calculate the secant of ``Quantity`` objects."""
    assert q.sec() == NotImplemented


@given(quantities(), rounding())
def test_asec_hypothesis(q, r):
    """Should calculate the inverse secant of ``Quantity`` objects."""
    assert q.asec() == NotImplemented


@given(quantities(), rounding())
def test_cot_hypothesis(q, r):
    """Should calculate the cotangent of ``Quantity`` objects."""
    assert q.cot() == NotImplemented


@given(quantities(), rounding())
def test_acot_hypothesis(q, r):
    """Should calculate the inverse cotangent of ``Quantity`` objects."""
    assert q.acot() == NotImplemented


# Hyperbolic function tests.
@given(quantities(), rounding())
def test_sinh_hypothesis(q, r):
    """Should calculate the hyperbolic sine of ``Quantity`` objects."""
    assert q.sinh() == NotImplemented


@given(quantities(), rounding())
def test_asinh_hypothesis(q, r):
    """Should calculate the inverse hyperbolic sine of ``Quantity`` objects."""
    assert q.asinh() == NotImplemented


@given(quantities(), rounding())
def test_cosh_hypothesis(q, r):
    """Should calculate the hyperbolic cosine of ``Quantity`` objects."""
    assert q.cosh() == NotImplemented


@given(quantities(), rounding())
def test_acosh_hypothesis(q, r):
    """Should calculate the inverse hyperbolic cosine of ``Quantity`` objects."""
    assert q.acosh() == NotImplemented


@given(quantities(), rounding())
def test_tanh_hypothesis(q, r):
    """Should calculate the hyperbolic tangent of ``Quantity`` objects."""
    assert q.tanh() == NotImplemented


@given(quantities(), rounding())
def test_atanh_hypothesis(q, r):
    """Should calculate the inverse hyperbolic tangent of ``Quantity`` objects."""
    assert q.atanh() == NotImplemented


@given(quantities(), rounding())
def test_csch_hypothesis(q, r):
    """Should calculate the hyperbolic cosecant of ``Quantity`` objects."""
    assert q.csch() == NotImplemented


@given(quantities(), rounding())
def test_acsch_hypothesis(q, r):
    """Should calculate the inverse hyperbolic cosecant of ``Quantity`` objects."""
    assert q.acsch() == NotImplemented


@given(quantities(), rounding())
def test_sech_hypothesis(q, r):
    """Should calculate the hyperbolic secant of ``Quantity`` objects."""
    assert q.sech() == NotImplemented


@given(quantities(), rounding())
def test_asech_hypothesis(q, r):
    """Should calculate the inverse hyperbolic secant of ``Quantity`` objects."""
    assert q.asech() == NotImplemented


@given(quantities(), rounding())
def test_coth_hypothesis(q, r):
    """Should calculate the hyperbolic cotangent of ``Quantity`` objects."""
    assert q.coth() == NotImplemented


@given(quantities(), rounding())
def test_acoth_hypothesis(q, r):
    """Should calculate the inverse hyperbolic cotangent of ``Quantity`` objects."""
    assert q.acoth() == NotImplemented
