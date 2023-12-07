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

"""Quantity class for significant figure calculations."""

import math
from decimal import ROUND_HALF_UP
from decimal import Decimal


def _most_significant_place(num):
    """Find the most significant place of a number.

    Find the most significant place of a number and return it as the
    exponent for a power of ten corresponding to the place value.

    Parameters
    ----------
    num : Decimal
        The number whose most significant place is needed.

    Returns
    -------
    Decimal
        The exponent of the most significant place.
    """
    return Decimal(math.floor(math.log10(abs(num))))


def _least_significant_place(num):
    """Find the least significant place of a number.

    Find the least significant place of a number and return it as the
    exponent for a power of ten corresponding to the place value.

    Parameters
    ----------
    num : Decimal
        The number whose least significant place is needed.

    Returns
    -------
    Decimal
        The exponent of the least significant place.
    """
    place = _most_significant_place(num)
    rem = abs(num) % Decimal(f"1e{place}")
    while rem > 0:
        place -= 1
        rem = rem % Decimal(f"1e{place}")
    return place


class Quantity:
    """A quantity for significant figure calculations."""

    def __init__(self, value, figures, rounding=ROUND_HALF_UP):
        """Initialize a ``Quantity()``."""
        self.value = Decimal(str(value))
        self.reported = self.value
        self.figures = Decimal(str(figures))
        self.rounding = rounding

    # Output operations.
    def __repr__(self):
        """Represent a ``Quantity``."""
        return f"Quantity({self.value}, {self.figures}, {self.rounding})"

    # Unary operations.
    def __neg__(self):
        """Negate a ``Quantity()`` object."""
        return Quantity(-self.value, self.figures)

    def __pos__(self):
        """Return a ``Quantity()`` object."""
        return Quantity(self.value, self.figures)

    def __abs__(self):
        """Calculate the magnitude of a ``Quantity()`` object."""
        return Quantity(abs(self.value), self.figures)

    # Comparisons.
    def __eq__(self, other):
        """Calculate the magnitude of a ``Quantity()`` object."""
        if (
            isinstance(other, Quantity)
            and self.value == other.value
            and self.figures == other.figures
        ):
            return True

        return False

    # Arithmetic operations.
    def __add__(self, other):
        """Add two ``Quantity()`` objects."""
        if isinstance(other, Quantity):
            value = self.value + other.value
            least = max(
                _most_significant_place(self.value) - self.figures + 1,
                _most_significant_place(other.value) - other.figures + 1,
            )
            most = max(
                _most_significant_place(value),
                _most_significant_place(value.quantize(Decimal(f"1e{least}"))),
            )
            return Quantity(value, most - least + 1)

        return NotImplemented

    def __sub__(self, other):
        """Subtract two ``Quantity()`` objects."""
        return self + -other

    def __mul__(self, other):
        """Multiply two ``Quantity`` objects."""
        if isinstance(other, Quantity):
            return Quantity(self.value * other.value, min(self.figures, other.figures))

        return NotImplemented

    def __truediv__(self, other):
        """Divide two ``Quantity`` objects."""
        if isinstance(other, Quantity):
            return Quantity(self.value / other.value, min(self.figures, other.figures))

        return NotImplemented
