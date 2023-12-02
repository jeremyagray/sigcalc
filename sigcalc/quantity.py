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

from decimal import ROUND_HALF_UP
from decimal import Decimal


class Quantity:
    """A quantity for significant figure calculations."""

    def __init__(self, value, figures, rounding=ROUND_HALF_UP):
        """Initialize a ``Quantity()``."""
        self.value = Decimal(str(value))
        self.reported = self.value
        self.figures = Decimal(str(figures))
        self.rounding = rounding

    # Output operations.

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
            return Quantity(self.value + other.value, self.figures)

        return NotImplemented

    def __sub__(self, other):
        """Subtract two ``Quantity()`` objects."""
        return self + -other

    def __mult__(self, other):
        """Multiply two ``Quantity`` objects."""
        raise NotImplementedError

    def __div__(self, other):
        """Divide two ``Quantity`` objects."""
        raise NotImplementedError
