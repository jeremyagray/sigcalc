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
    if num == Decimal("0"):
        return Decimal("0")

    return Decimal(math.floor(math.log10(abs(num))))


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
            Rounding mode selected from the modes in ``decimal``.
        """
        self.value = Decimal(str(value))
        self.reported = self.value
        if not constant:
            self.figures = Decimal(str(figures))
        else:
            self.figures = getcontext().prec
        self._constant = constant
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

    def __format__(self, specifier):
        """Format a ``Quantity`` object.

        Format a ``Quantity`` object, rounding to significant figures
        first and then passing any format specifier through to
        ``Decimal().__format__()`` for formatting.
        """
        return format(self._round(), specifier)

    def __str__(self):
        """Stringify a ``Quantity`` object.

        Stringify a ``Quantity`` object, rounding to significant
        figures first and then using ``Decimal().__str__()`` for
        stringification.
        """
        return str(self._round())

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
    def __lt__(self, other):
        """Determine the ordering of two ``Quantity()`` objects."""
        if isinstance(other, Quantity) and self._round() < other._round():
            return True

        return False

    def __le__(self, other):
        """Determine the ordering of two ``Quantity()`` objects."""
        return self.__lt__(other) or self.__eq__(other)

    def __eq__(self, other):
        """Determine equality of two ``Quantity()`` objects."""
        if (
            isinstance(other, Quantity)
            and self._round() == other._round()
            and self.figures == other.figures
        ):
            return True

        return False

    def __ne__(self, other):
        """Determine the inequality of two ``Quantity()`` objects."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Determine the ordering of two ``Quantity()`` objects."""
        return not self.__lt__(other) and self.__ne__(other)

    def __ge__(self, other):
        """Determine the ordering of two ``Quantity()`` objects."""
        return not self.__lt__(other)

    # Arithmetic operations.
    def __add__(self, other):
        """Add two ``Quantity()`` objects."""
        if isinstance(other, Quantity):
            value = self.value + other.value

            if self.constant and other.constant:
                return Quantity(value, getcontext().prec, constant=True)
            elif self.constant and not other.constant:
                least = _most_significant_place(other.value) - other.figures + 1
            elif other.constant and not self.constant:
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
            if self.constant and other.constant:
                return Quantity(
                    self.value * other.value, getcontext().prec, constant=True
                )
            elif self.constant and not other.constant:
                return Quantity(self.value * other.value, other.figures)
            elif other.constant and not self.constant:
                return Quantity(self.value * other.value, self.figures)
            else:
                return Quantity(
                    self.value * other.value, min(self.figures, other.figures)
                )

        return NotImplemented

    def __truediv__(self, other):
        """Divide two ``Quantity`` objects."""
        if isinstance(other, Quantity):
            if self.constant and other.constant:
                return Quantity(
                    self.value / other.value, getcontext().prec, constant=True
                )
            elif self.constant and not other.constant:
                return Quantity(self.value / other.value, other.figures)
            elif other.constant and not self.constant:
                return Quantity(self.value / other.value, self.figures)
            else:
                return Quantity(
                    self.value / other.value, min(self.figures, other.figures)
                )

        return NotImplemented

    @property
    def constant(self):
        """Mark a ``Quantity`` as a constant with unlimited precision."""
        return self._constant

    @constant.setter
    def constant(self, value):
        """Set a ``Quantity`` object's ``constant`` property.

        Set a ``Quantity`` object's ``constant`` property to value, if
        boolean.
        """
        if isinstance(value, bool):
            self._constant = value

    def _round(self):
        """Round a ``Quantity`` object ``value`` to significant figures.

        Round a ``Quantity`` object ``value`` to significant figures
        using the current rounding mode, returning a ``Decimal``.
        Return ``self.value`` unrounded if ``self.constant`` is
        ``True``.

        Returns
        -------
        Decimal
            The rounded ``value`` of the ``Quantity``.
        """
        if self.constant:
            return self.value

        place = _most_significant_place(self.value) - self.figures + Decimal(1)
        return self.value.quantize(Decimal(f"1e{place}"), rounding=self.rounding)

    def round(self):  # dead: disable
        """Round a ``Quantity`` object to significant figures.

        Round a ``Quantity`` object to significant figures using the
        current rounding mode, returning a new ``Quantity`` with only
        the rounded significant figures.  Return a new ``Quantity``
        equal to ``self`` unrounded if ``self.constant`` is ``True``.

        Returns
        -------
        Quantity
            A new ``Quantity`` equal to the rounded ``self``.
        """
        if self.constant:
            return Quantity(self.value, self.figures, self.constant, self.rounding)

        return Quantity(self._round(), self.figures, self.constant, self.rounding)
