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
from decimal import getcontext


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

    def __init__(self, value, figures, constant=False, rounding=ROUND_HALF_UP):
        """Initialize a ``Quantity()``.

        Parameters
        ----------
        value : str
            Value of the quantity, to be converted to a ``Decimal``.
        figures : str
            Significant figures of the quantity, to be converted to a
            ``Decimal``.
        constant : boolean
            Set as constant (unlimited precision), or not.
        rounding : str
            Rounding mode selected fromt the modes in ``decimal``.
        """
        self.value = Decimal(str(value))
        self.reported = self.value
        if not constant:
            self.figures = Decimal(str(figures))
        else:
            self.figures = getcontext().prec
        self.constant = constant
        self.rounding = rounding

    # Output operations.
    def __repr__(self):
        """Represent a ``Quantity``."""
        rep = f'Quantity("{self.value}", "{self.figures}"'

        if self.constant:
            rep += f", constant={self.constant}"

        if self.rounding != ROUND_HALF_UP:
            rep += f", rounding={self.rounding}"

        return rep + ")"

    # Unary operations.
    def __neg__(self):
        """Negate a ``Quantity()`` object."""
        return Quantity(-self.value, self.figures, self.constant, self.rounding)

    def __pos__(self):
        """Return a ``Quantity()`` object."""
        return Quantity(self.value, self.figures, self.constant, self.rounding)

    def __abs__(self):
        """Calculate the magnitude of a ``Quantity()`` object."""
        return Quantity(abs(self.value), self.figures, self.constant, self.rounding)

    # Comparisons.
    def __eq__(self, other):
        """Calculate the magnitude of a ``Quantity()`` object."""
        if (
            isinstance(other, Quantity)
            and self.constant == other.constant
            and self.rounding == other.rounding
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

            if self.is_constant() and other.is_constant():
                return Quantity(value, getcontext().prec, constant=True)
            elif self.is_constant() and not other.is_constant():
                least = _most_significant_place(other.value) - other.figures + 1
            elif other.is_constant() and not self.is_constant():
                least = _most_significant_place(self.value) - self.figures + 1
            else:
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
            if self.is_constant() and other.is_constant():
                return Quantity(
                    self.value * other.value, getcontext().prec, constant=True
                )
            elif self.is_constant() and not other.is_constant():
                return Quantity(self.value * other.value, other.figures)
            elif other.is_constant() and not self.is_constant():
                return Quantity(self.value * other.value, self.figures)
            else:
                return Quantity(
                    self.value * other.value, min(self.figures, other.figures)
                )

        return NotImplemented

    def __truediv__(self, other):
        """Divide two ``Quantity`` objects."""
        if isinstance(other, Quantity):
            if self.is_constant() and other.is_constant():
                return Quantity(
                    self.value / other.value, getcontext().prec, constant=True
                )
            elif self.is_constant() and not other.is_constant():
                return Quantity(self.value / other.value, other.figures)
            elif other.is_constant() and not self.is_constant():
                return Quantity(self.value / other.value, self.figures)
            else:
                return Quantity(
                    self.value / other.value, min(self.figures, other.figures)
                )

        return NotImplemented

    def is_constant(self):
        """Determine if a ``Quantity`` is a constant."""
        return self.constant

    def create_constant(self):  # dead: disable
        """Convert a ``Quantity`` into a constant.

        Convert ``self`` into a constant.

        Returns
        -------
        Quantity
            A new ``Quantity`` object equal to ``self`` and converted
            to a constant.
        """
        self.constant = True
        return Quantity(self.value, getcontext().prec, self.constant, self.rounding)
